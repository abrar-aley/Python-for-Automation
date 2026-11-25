import os

path = "D:\\Learnings\\Full Stack Practice"
print(os.listdir(path))
dcount = 0
fcount = 0

filess = []
folders = []

for root,dirs,files in os.walk(path):

    if ".git" in dirs:
        dirs.remove(".git")

    for folder in dirs:
        dcount+=1
        folders.append(folder)

    for file in files:
        fcount+=1
        filess.append(file)

    


print("FILES:  ")
print("No of files= ",fcount)
for file in filess:
    print(file)


print("FOLDERS:  ")
print("No of folders= ",dcount)
for folder in folders:
    print(folder)
