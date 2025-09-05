# Write a python program to print the contents of a directory using the os module search for online the function which does that

import os

directory_path = '/New folder'

contents = os.listdir(directory_path)

for item in contents:
    print(item)