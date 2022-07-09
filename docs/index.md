# remove-folder and copy-folder scripts

The **remove-folder** and **copy-folder** scripts can be used to automate the process of copying files from one folder into another folder on Windows.🤖

1. **remove-folder script:** Deletes the existing folder specified in the script. The folder name you want to delete should match the name of the folder you want to copy in the **copy-folder** script.
2. **copy-folder script:** Copies the folder specified in the script to the location specified in the script.

> **Warning**
> 
> This script only runs properly if the destination (dest) path doesn't already exist. If the folder with the same name exists, this script will not run properly. 

You can configure Task Scheduler in Windows to automate the process of running these scripts. For details on using Task Scheduler, please see [Task Scheduler for developers](https://docs.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page).
