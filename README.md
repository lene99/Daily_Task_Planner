<h1>:heavy_check_mark::date: Daily Task Planner :pencil2: </h1>

<h2> Preview: </h2>
<img src="https://user-images.githubusercontent.com/89850402/214809955-9dd4d73a-2f6d-4297-868c-b4cdcb1d1bf6.png" width="600px" height="500px" alt="Daily Task Planner Visual">

<h2> Tools Utilized: </h2>
<p align="middle">
<img src=https://user-images.githubusercontent.com/89850402/214824237-48470708-4300-4e5c-8d2a-b86a683f5d32.png width="200px" height="200px"/>  
<img src=https://user-images.githubusercontent.com/89850402/214824141-e2c86c45-24e0-4b08-9eee-d419e972c87a.png width="400px" height="200px"/>
<img src=https://user-images.githubusercontent.com/89850402/214824059-c1b95721-6bfc-417f-901b-9f8e628cf220.png width="400px" height="200px"/>

</p>


<p> Daily Task Planner is created using QtDesigner Tools, Python 3.9.0, and SQLite 3.32.2 for the backend. </p>

<h2> Background </h2>
<p> A little bit of backstory to this personal project, I was actually lazy to look for applications / programs on the Internet to keep track of my daily tasks. Windows Sticky Notes has always been my go-to app for me to keep track of tasks. However, there were certain limitations to using Sticky Note for this purpose, and figured that I should create my own to-do task planner with the use of some simple Python code and the QtDesigner tool. </p>

<h2> Program Features </h2>
<p> In the current version of the tool (V1), the main functionalities are: </p>
<table>
<tr>
<td> Feature </td>
<td> Description </td>
</tr>
<tr style="width=500px; height=500px"> 
<td> <img src="https://user-images.githubusercontent.com/89850402/214816210-f390806e-a6e7-4f35-a5e0-d312a90f968b.png" alt="Insert Task Button"> </td>
<td> User can type in their task into the "Insert Text" box and then click "Add New" to add a new task to the list for that specific day. </td>
</tr>
<tr> 
<td> <img src="https://user-images.githubusercontent.com/89850402/214818527-885b44de-a206-4d71-824c-3821f9127386.png" alt="Show Today Button"> </td>
<td> User can click on "Show Today" button for the calendar to focus on today's date and tasks. </td>
</tr>
<tr> 
<td> <img src="https://user-images.githubusercontent.com/89850402/214819907-8c998925-f2b9-4a04-96d4-97785e85d07f.png" alt="Task Checkbox"> </td>
<td> User can check the task that is done. </td>
</tr>
<tr> 
<td> <img src="https://user-images.githubusercontent.com/89850402/214818756-3c334a38-1477-4bc1-8599-664b2222fe72.png" alt="Save Changes Button"> </td>
<td> User can click on "Save Changes" button whenever they check/uncheck a task to save the state in the backend. </td>
</tr>
<tr> 
<td> <img src="https://user-images.githubusercontent.com/89850402/214818858-2974eb63-082f-41c5-a2c1-bc48b5e0617f.png" alt="Delete Task Button"> </td>
<td> User can click on "Delete Task" <b>once</b> they have selected a task from the list to delete it. If the user did not select a task, an alert message will pop-up telling the user to select a task before deleting it. </td>
</tr>
<tr> 
<td> <img src="https://user-images.githubusercontent.com/89850402/214819098-55b69378-6b5c-4a04-ba05-c1b575044fdf.png" alt="Calendar"> </td>
<td> User can click on any of the dates on the Calendar and the new task list for that date will be shown on the right. User can also toggle left or right green arrow buttons to move to the months before or after the current one. They can also click on the current month and year to change them respectively to whichever month/year they want. </td>
</tr>
<tr> 
<td> <img src="https://user-images.githubusercontent.com/89850402/214819436-657d10f5-b34c-4a87-aee2-7f3a2946190e.png" alt="Task List"> </td>
<td> The list of tasks which appear on the right of the program. This is where user will be able to see the tasks they have added for that specific day. </td>
</tr>
</table>

<h2> Getting Started </h2>

1. Clone the repository into your local disk
2. Create a virtual environment in the same directory.
3. In the virtual environment, download PyQt5 using ```pip install pyqt5```
4. Then, download PyQt5-Tools using ```pip install pyqt5-tools```
5. Download SQLite3 <a href="https://www.sqlite.org/2022/sqlite-dll-win64-x64-3400100.zip">here</a>. 
6. Lastly, if you have yet to, download Python 3.9.0. in your virtual environment. 
7. Run the main.py file.

<h2> Additional Information </h2>
<p> For it to be useful, I've also created a .bat file which opens up the program everytime i start up my computer so that I can be reminded of what are the tasks I would need to complete for the day. (Hopefully this will also make me become more disciplined as compared to before with the Sticky Notes!)
  
<p> Upcoming version 2 will include some other additional functionalities. My ultimate goal for this program is to slowly expand it to become an AiO program which lets me manage my tasks, set reminders, grocery list, keeping track of my current toiletries usage, expiry dates, etc. Once I am fully satisfied with the program, I will package it into an executable file so that my peers can just download the .exe file to use it, instead of having to do the technical steps, especially for those havev limited knowledge on git functionalities. </p> 
