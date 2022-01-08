# some examp;e python code linking what we learned in class to some new code
# 0be used as a  learning example
# By Donato Kava
import subprocess
#import subprocess


print("module is running")

# By default the python subpress.run() command on windows is running the
# command prompt program that has a different santax from powershell.
# (e.g "ls" = "dir")
# if you want to find more commands here is the online resource.

# The code below is more simple but since we learned powershell and its newer
# I pnly list it so you can see the differnece and be aware.
# list_files = subprocess.call("dir", shell=True)
# print("The exit code was: %d" % list_files)

list_files = subprocess.run(["powershell", "-command", "ls"])

# CHALLANGE try to get this to run without errors showing up when the file
# already exists

# Make a new folder to place some files into
list_files = subprocess.run(["powershell", "-command", "mkdir", "file_folder"])

# Change the active director to the new folder, How could you skip this step?
list_files = subprocess.run(["powershell", "-command", "cd", "./file_folder"])
# Display the directory to show the change
list_files = subprocess.run(["powershell", "-command", "ls"])

# CHALLANGE try to make this range base on something else.
for x in range(0, 3):
    # CHALLANGE Try changing New-item to common typos to see what errors you
    # get (e.g try putting in new_item)

    # *****************************************************
    # ** Notice how i put the folder in new-item name.   **
    #    The command is new-item ./file_folder/file#.txt **
    # *****************************************************

    # place command here
    # this is a string contructor example below
    list_files = subprocess.run(
        ["powershell", "-command", "New-Item", "./file_folder/file_" + str(x) + ".txt"])
    # Display the directory to show the change
    list_files = subprocess.run(
        ["powershell", "-command", "ls", "./file_folder"])
    #conditional example
    if(x == 2):
        print("I only print the last time")
        x = 3
        print("for loop", x)
    print(x)

print("Module Finished")
