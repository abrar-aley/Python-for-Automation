import os

os.chdir("D:\\")
os.makedirs(os.path.join("D:","OS_PRACTISE_FOLDER","practise__file.txt"))

print(os.path.exists("D:\\OS_PRACTISE_FOLDER\\practise__file.txt"))