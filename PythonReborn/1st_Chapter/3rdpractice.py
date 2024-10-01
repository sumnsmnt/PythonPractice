# Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that. 

import os

# Specify the directory you want to list
directory_path = 'D:\Python 100 days\PythonReborn\Chapter1'

try:
    # List all files and directories in the specified path
    contents = os.listdir(directory_path)
    
    print("Contents of the directory:")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory {directory_path} does not exist.")
except PermissionError:
    print(f"Permission denied to access the directory {directory_path}.")
