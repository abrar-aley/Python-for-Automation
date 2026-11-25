import os

path="D:/Learnings/notes/report.txt"
""""""""""
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.split(path))
print(os.path.splitext(path))
print(os.path.exists(path))
print(os.path.isfile(path))
print(os.path.isdir(path))
"""""

print(os.path.exists("D:\\Learnings\\Python Projects AI-OLD\\Conditionals_and_Booleans"))
print(os.path.isfile("D:\\Learnings\\Python Projects AI-OLD\\Conditionals_and_Booleans\\Age_Checker.py"))
print(os.path.isdir("D:\\Learnings\\Python Projects AI-OLD\\Conditionals_and_Booleans"))