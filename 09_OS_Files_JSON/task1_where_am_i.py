import os

print("Before:", os.getcwd())

p = "D:/Learnings/sandbox"

if not os.path.exists(p):
    os.mkdir(p)

os.chdir(p)
print("In sandbox:", os.getcwd())
print(os.listdir())

# Now go to the folder where the task files live
os.chdir("D:/Learnings/Python-for-Automation/09_OS_Files_JSON")
print("Now in:", os.getcwd())
print(os.listdir())