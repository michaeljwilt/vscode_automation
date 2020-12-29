import os

# Initial input for Folder Creation
fileName = input(" Enter file name ")
path = "/Users/michaelwilt/Desktop/" + fileName


# Creation of new Directory
try:
    os.mkdir(path)
except OSError:
    print("Creation of the directory %s failed" % path)
else:
    print("Successfully created the directory %s " % path)


# Call Directory and Open in VS Code
os.chdir("/Users/michaelwilt/Desktop/" + fileName)
cwd = os.getcwd()
os.system("code .")


# ATTEMPTS TO TRY BASIC GIT COMMANDS
# try:
#     os.system("git init")
#     os.system("git add .")
#     os.system("git commit -m 'Initial Commit'")

# except OSError:
#     print("Creation of the git repository %s failed")
# else:
#     print("Successfully created the git repository %s ")
