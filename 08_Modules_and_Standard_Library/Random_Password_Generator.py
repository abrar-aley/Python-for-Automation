import random
import string

digits=['0','1','2','3','4','5','6','7','8','9']
characters=['`','!','@','#','$','%','^','&','*']

def Generate_Password():
    password=''
    for i in range(8):
        category= random.choice([digits, characters, string.ascii_letters])
        char= random.choice(category)
        password+=char
    return password

print('Random password is: ',Generate_Password())
