"""
Rename More than one file in a directory.
NOTE: BELOW CODE IS STILL STATIC.
"""
import os                           # Import OS Package

try:
    os.chdir('D:/DataScience/')     # Path of File
    print(os.getcwd())              # Return Current Working Directory

    lst_dir = os.listdir()          # List Directory
    for file_name in lst_dir:
        if file_name.split(" ", 1)[0][0] == "[" and \
           file_name.split(" ", 1)[0][-1] == "]" in file_name:
            os.rename(src=file_name, dst=file_name.split(" ", 1)[1])
            print(file_name)
except OSError as err:  # File Not Found Error
    print("Exception: {}".format(err))
