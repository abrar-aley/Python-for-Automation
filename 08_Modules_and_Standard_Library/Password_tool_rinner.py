import password_tool as pt

password1=pt.Generate_password(6)
print('password 1: ',password1)
print('password 1 strength: ',pt.validate_pasword(password1))

password2=pt.Generate_password(8)
print('password 2: ',password2)
print('password 2 strength: ',pt.validate_pasword(password2))