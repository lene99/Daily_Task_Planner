# QWidget represents the widget we created (The Designer) and QApplication to launch the application.
import os
from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox
# loadUi enable us to load our UI file that you created in the designer INTO our code
from PyQt5.uic import loadUi
# use sys to pass arguments & execute the application
import sys 

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QDate

import sqlite3

# scales window size to fit the GUI 
os.environ['QT_AUTO_SCREEN_SCALE_FACTOR'] = '1'

# create a list of tasks
tasks = ["Write email", "Finish feature","Watch tutorial"]

basedir = os.path.dirname(__file__)

# inherit QWidget 
class Window(QWidget):
    # Constructor for Window class. 
    # Call the constructor for this superclass (QWidget) using super 
    def __init__(self):
        super(Window, self).__init__() # this inherits all the methods & variables in the superclass, QWidget into this class.
        loadUi("main.ui", self) 
        self.setWindowTitle("Daily Task Planner - Created by Jolene")
        self.calendarWidget.selectionChanged.connect(self.calendarDateChanged)
        # calling it as soon as you initialize the object 
        self.calendarDateChanged()
        self.saveButton.clicked.connect(self.saveChanges)
        self.addButton.clicked.connect(self.addNewTask)
        self.deleteTaskButton.clicked.connect(self.deleteTask)
        self.showTodayButton.clicked.connect(self.showToday)
    
    def calendarDateChanged(self):
        print("The calendar date was changed.")
        dateSelected = self.calendarWidget.selectedDate().toPyDate()
        # .toPyDate() converts the date to a string format 
        # .strftime("%m-%d") formats the date to a specific format that I want (%m - month, %d - day, %y - year)
        print("Date selected:", dateSelected)
        self.updateTaskList(dateSelected)
    
    def updateTaskList(self, date):
        # before we update the date we want to clear the list 
        self.tasksListWidget.clear()
        # connect to SQLITE3 database
        db = sqlite3.connect("data.db")
        # cursor will query the database
        cursor = db.cursor() 

        # define my query (what do I want my DB to return me?)
        query = "SELECT task, completed FROM tasks WHERE date = ?"

        # contain the actual value for the date (must be a tuple)
        row = (date,)
        # fetchall() as we can have more than 1 tasks per day
        results = cursor.execute(query, row).fetchall()
        for result in results:
            # add them to the list widget 
            item = QListWidgetItem(str(result[0])) # result[0] is the task, result[1] is completed
            # setFlags is like giving a property to a object
            # ItemIsUserCheckable => We want the item to be checkable.
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            if result[1] == "YES":
                item.setCheckState(QtCore.Qt.Checked)
            elif result[1] == "NO":
                # set the box to be unchecked
                item.setCheckState(QtCore.Qt.Unchecked)
            self.tasksListWidget.addItem(item)
    
    def saveChanges(self):
        # update the information in the database
        
        # connect to DB again
        db = sqlite3.connect("data.db")
        cursor = db.cursor() 
        date = self.calendarWidget.selectedDate().toPyDate()

        for i in range(self.tasksListWidget.count()):
            item = self.tasksListWidget.item(i)
            # convert the item to a string (Representative of a task) [CANNOT USE str(item)]
            task = item.text()
            # check if a box is checked or not
            if item.checkState() == QtCore.Qt.Checked:
                query = "UPDATE tasks SET completed = 'YES' WHERE task = ? AND date = ?"
            else: 
                query = "UPDATE tasks SET completed = 'NO' WHERE task = ? AND date = ?"
            row = (task,date,)
            cursor.execute(query, row)
        # commit my changes to the database
        db.commit()

        # Pop-up alert message when Save Changes button is clicked. 
        messageBox = QMessageBox()
        messageBox.setText("Changes saved.")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()

    def addNewTask(self):
        # connect to DB again
        db = sqlite3.connect("data.db")
        cursor = db.cursor() 
        newTask = str(self.taskLineEdit.text())
        if (newTask != ''):

            date = self.calendarWidget.selectedDate().toPyDate()

            query = "INSERT INTO tasks(task, completed, date) VALUES (?,?,?)"
            row = (newTask, "NO", date,)

            cursor.execute(query, row)
            db.commit()
            self.updateTaskList(date)
            self.taskLineEdit.clear()
        else: 
            messageBox = QMessageBox()
            messageBox.setWindowTitle("Daily Task Planner - Created by Jolene")
            messageBox.setText("Please enter a name for the new task.")
            messageBox.setStandardButtons(QMessageBox.Ok)
            messageBox.exec()
    
    def deleteTask(self): 
        

        if(self.tasksListWidget.currentItem()):
            # connect to DB again
            db = sqlite3.connect("data.db")
            cursor = db.cursor() 
            task = str(self.tasksListWidget.currentItem().text()) 
            print(task)
            date = self.calendarWidget.selectedDate().toPyDate()
            query = "DELETE FROM tasks WHERE task = ?"
            row = (task,)
            cursor.execute(query, row)
            db.commit() 
            messageBox = QMessageBox()
            messageBox.setWindowTitle("Daily Task Planner - Created by Jolene")
            messageBox.setText("Task deleted successfully!")
            messageBox.setStandardButtons(QMessageBox.Ok)
            messageBox.exec()
            self.updateTaskList(date)
        else:
            messageBox = QMessageBox()
            messageBox.setWindowTitle("Daily Task Planner - Created by Jolene")
            messageBox.setText("You did not select an item to delete!")
            messageBox.setStandardButtons(QMessageBox.Ok)
            messageBox.exec()
        
    def showToday(self):
        # get today's date
        today = QDate().currentDate()
        # set the date on calendarWidget using .setSelectedDate(<date>)
        self.calendarWidget.setSelectedDate(today)

        


if __name__ == "__main__":
    
    # Passing the command line arguments into the creation of this QApplication
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(os.path.join(basedir, 'app-logo.ico')))
    window = Window()
    # show this QWidget
    window.show()
    sys.exit(app.exec())