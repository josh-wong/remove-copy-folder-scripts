# Python program to explain shutil.copytree() method 
# This script only runs properly if the destination (dest) path doesn't already exist.
# If the folder with the same name exists, this script will not run properly.

# importing os module
import os
# importing shutil module 
import shutil

# Path: the parent folder where the files to be copied originate from
path = "<INSERT FULL FOLDER PATH>"

print("Before copying file:")
print(os.listdir(path))

# Source: the folder where the files to be copied originate from
src = "<INSERT FULL FOLDER PATH>"

# Destination: the folder where the files should be copied to
dest = "<INSERT FULL FOLDER PATH>"

# Copy the content of source to destination
destination = shutil.copytree(src, dest)
 
print("After copying file:")
print(os.listdir(path))
 
# Print path of newly created file
print("Destination path:", destination)
