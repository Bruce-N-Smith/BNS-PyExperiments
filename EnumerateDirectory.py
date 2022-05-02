# This is a learning exercise, not real code, that is why comments are verbose

# Import the external library called OS so that its functions/methods are available to use locally
import os

# Create a variable called PATH to hold the directory path
path ='/users/REPLACE-WITH-YOUR-USER-NAME'

# Create a for loop and use the WALK method in the OS library to retrieve data about folders and files in the path specified above
# It appears we've created 3 more variables called ROOT, DIRECTORIES, and FILES here...?
# It appears we've created 1 more variable called NAME here too...?
# In the WALK method we've specified FALSE for the TOPDOWN parameter, so the program works from the bottom up the tree
# Finally we use the PRINT function and use the PATH.JOIN method in the OS library to concatenate the path name and the object name 
for root, directories, files in os.walk(path, topdown=False):
    for name in files:
        print(os.path.join(root, name))
    for name in directories:
        print(os.path.join(root, name))