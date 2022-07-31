# How to configure the remove-folder and copy-folder scripts

This document describes how to set up both the remove-folder script and the copy-folder script, and provides a reference for using Task Scheduler in Windows to automate this script.

> **Warning**
> 
> For the copy-folder script to work, the destination folder must not include a folder with the same name. Therefore, the purpose of the remove-folder script is to remove a folder with the existing name so that the folder in a different location can be copied.
> 
> If you are using GitHub or GitLab, only the changes between files should sync when committing changes to a branch.

## Configure the remove-folder script 

On your computer, create a text file.

Give that file a name that you can easily recognize and understand in the future. For example, you might name the file "documents-remove-folder.py" if you'll be removing files from your "Documents" folder. Save the file with the extension ".py" so that the file changes from being a text file to a Python file.

Copy the contents of [remove-folder.py](https://github.com/josh-wong/remove-copy-folder/blob/main/remove-folder.py) into the Python file you just created on your computer.

In the script, replace the instances of `<INSERT FULL FOLDER PATH>` as specified in the comments in the script. Make sure you use forward slashes (`/`) between the folder names in the path.

Then, save your changes.

## Configure the copy-folder script 

On your computer, create a text file. 

Give that file a name that you can easily recognize and understand in the future. For example, you might name the file "documents-copy-folder.py" if you'll be copying files from your "Documents" folder. Save the file with the extension ".py" so that the file changes from being a text file to a Python file.

Copy the contents of [copy-folder.py](https://github.com/josh-wong/remove-copy-folder/blob/main/copy-folder.py) into the Python file you just created on your computer.

In the script, replace the instances of `<INSERT FULL FOLDER PATH>` as specified in the comments in the script. Make sure you use forward slashes (`/`) between the folder names in the path.

Then, save your changes.

## Automate these scripts

To automate the remove-folder and copy-folder scripts, you can add a task for each script in Task Scheduler in Windows. Unfortunately, because multiple environment setups exist depending on how you use Windows, this tutorial does not describe setting up tasks in Task Scheduler.

For details on using Task Scheduler, please see [Task Scheduler for developers](https://docs.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page).