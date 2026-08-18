Based on the book Automate The Boring Stuff with Python.

### Scripts
1. Phone and Email python script finds phone numbers and email addresses on the clipboard. Useful if searching in a webpage or resume, you can hit select all (ctrl+A), then copy (ctrl+C for Windows users) and then run the script. It will print in the console if there is any email and/or phone number in the copied text. It will also add it to the clipboard, so you can open a text file and paste the results.

2. Multiplication Quiz is a script that generates 5 multiplication questions.

### How to have an easier access the script by creating a Batch file? 
For my case, the folder at C:\Users\%USERNAME%\BatchScripts contains both the .py and .bat file needed to run the script from a run command (Windowskey + R). 
For this to work, the above address have to be in the path environment variables. You can access by searching "path" or "edit system" in the windows search bar. 
A small windows shall open with System Properties as the windows title. Under Advanced, click Environment Variables. Highlight the Path from under the user variables and click Edit. Now add the path to the folder containing the .py and .bat files. 
Now that is added to the system path pressing Windowskey + R brings up the run command. Now write the name of the script (ex. multiplicationQuiz) without the extension, and it should run. 
