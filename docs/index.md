# remove-folder and copy-folder scripts🤖

!!! warning**
    
    These scripts only run properly if the destination (dest) path doesn't already exist. If the folder with the same name exists, this script will not run properly. 

By using the **remove-folder** and **copy-folder** scripts and configuring each script as a task in Task Scheduler in Windows, you can automate the process of copying files from one folder into another folder on Windows.

- **remove-folder script:** Deletes the existing folder specified in the script. The folder name you want to delete should match the name of the folder you want to copy in the **copy-folder** script.
- **copy-folder script:** Copies the folder specified in the script to the location specified in the script.

These scripts can be particularly helpful for when you want to automatically back up folders at a specific time.
