Based on the book Automate The Boring Stuff with Python.

### Scripts
1. <ins>Phone and Email python script</ins> finds phone numbers and email addresses on the clipboard. Useful if searching in a webpage or resume, you can hit select all (ctrl+A), then copy (ctrl+C for Windows users) and then run the script. It will print in the console if there is any email and/or phone number in the copied text. It will also add it to the clipboard, so you can open a text file and paste the results.

2. <ins>Multiplication Quiz</ins> is a script that generates 5 multiplication questions.

### How to have an easier access to the script by creating a Batch file? 
In my case, I have saved the folder at C:\Users\%USERNAME%\BatchScripts with both the .py and .bat file needed to run the script from a run command (Windowskey + R). 

So for this to work, the above address have to be in the path environment variables. You can edit this by searching "path" or "edit system" in the windows search bar. 
A small windows shall open with System Properties as the windows title. Under Advanced, click Environment Variables. Highlight the Path from under the user variables and click Edit. Now add the path to the folder containing the .py and .bat files. 

Now that is added to the system path, you can bring up the run command (Windowskey + R) and write the name of the script (ex. multiplicationQuiz) without the extension, and it should run. 
