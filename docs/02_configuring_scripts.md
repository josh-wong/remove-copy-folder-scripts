# How to configure the remove-folder and copy-folder scripts

The following describes how to set up both the remove-folder script and the copy-folder script. 

> **Warning**
> 
> For the copy-folder script to work, the destination folder must not include a folder with the same name. Therefore, the purpose of the remove-folder script is to remove a folder with the existing name so that the folder in a different location can be copied.
> 
> If you are using GitHub or GitLab, only the changes between files should sync when committing changes to a branch.

## Configure the remove-folder script 

On your computer, create a text file, then give that file a name that you can easily recognize and understand in the future. For example, you might name the file "documents-remove-folder.py" if you'll be removing files from your "Documents" folder. Be sure to give that file the extension ".py" so that the file changes from being a text file to a Python file.

Copy the contents of [remove-folder.py](https://github.com/josh-wong/remove-copy-folder/blob/main/remove-folder.py) into the Python file you just created on your computer.

In the script, replace the instances of "\<INSERT FULL FOLDER PATH\>" as specified in the comments in the script. Make sure you use forward slashes (/) between the folder names in the path.

## Configure the copy-folder script 

On your computer, create a text file, then give that file a name that you can easily recognize and understand in the future. For example, you might name the file "documents-copy-folder.py" if you'll be copying files from your "Documents" folder. Be sure to give that file the extension ".py" so that the file changes from being a text file to a Python file.

Copy the contents of [copy-folder.py](https://github.com/josh-wong/remove-copy-folder/blob/main/copy-folder.py) into the Python file you just created on your computer.

In the script, replace the instances of "\<INSERT FULL FOLDER PATH\>" as specified in the comments in the script. Make sure you use forward slashes (/) between the folder names in the path.
