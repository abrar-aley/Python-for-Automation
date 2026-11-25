import os
os.chdir("D:\\Learnings")
print("inside: ",os.getcwd())
os.rename("abrar","ali")

os.rmdir("ali")

os.rmdir("practice") #cannot be removed because the directory is not empty