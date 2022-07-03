# Python program to explain shutil.copytree() method 

# importing shutil module 
import shutil

# Path: the parent folder where the files to be copied originate from
# This path must end with a slash.
path = '<INSERT FULL FOLDER PATH>/' 

# Source path: where the files to be copied originate from
src = '<INSERT FULL FOLDER PATH>'

# Destination path: where the files should be copied to
dest = '<INSERT FULL FOLDER PATH>'

# Copy the content of source to destination 
destination = shutil.copytree(src, dest) 

# print(destination) prints the path of newly created file