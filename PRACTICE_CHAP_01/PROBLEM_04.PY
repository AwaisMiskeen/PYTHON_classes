# Label the program written in problem_03 with comments

import os

# Select the directory whose content you want to list
directory_path = '/New folder'

# Use the os module to list the directory content
contents = os.listdir(directory_path)

# Prints the contents to the directory
for item in contents:
    print(item)