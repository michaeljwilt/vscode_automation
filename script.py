import os

fileName = input(" Enter file name ")
path = "/Users/michaelwilt/Desktop/" + fileName

try:
    os.mkdir(path)
except OSError:
    print("Creation of the directory %s failed" % path)
else:
    print("Successfully created the directory %s " % path)

try:
    os.system("git init")
    os.system("git add .")
    os.system("git commit -m 'Initial Commit'")
except OSError:
    print("Creation of the directory %s failed" % path)
else:
    print("Successfully created the directory %s " % path)
