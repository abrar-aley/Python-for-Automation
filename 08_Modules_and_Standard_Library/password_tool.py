import random
import string

digits=['0','1','2','3','4','5','6','7','8','9']
characters=['`','!','@','#','$','%','^','&','*']

def Generate_password(length):
    password=''
    for i in range(length):
        category= random.choice([digits, characters, string.ascii_letters])
        char= random.choice(category)
        password+=char
    return password

def validate_pasword(password):
   has_digit=False
   has_special_characters=False
   has_upper_case=False

   for char in password:
       if char.isupper():
           has_upper_case= True

       if char.isdigit():
           has_digit=True

       if char in characters:
           has_special_characters=True

   if len(password)>=8:
       if has_digit==True:
           if has_special_characters==True:
               if has_upper_case==True:
                   return 'strong'

   else:
       return 'weak'
           

                            

    

