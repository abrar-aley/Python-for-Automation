import random

def roll_dice():
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    return dice1+dice2

Counts= {
   2:0,
   3:0,
   4:0,
   5:0,
   6:0,
   7:0,
   8:0,
   9:0,
   10:0,
   11:0,
   12:0
}

for i in range(10):
    num= roll_dice()
    print(num)
    Counts[num]+=1
    num=0

for key,values in Counts.items():
    print(key,'appeared',values,'times')
    