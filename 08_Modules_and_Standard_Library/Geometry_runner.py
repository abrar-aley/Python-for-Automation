import Geometry

operand= int(input("Enter number or radius: "))

print('--Menu--','1.find area','2.find circumference','3.check square root', sep="\n")
choise= int(input('Enter choise: '))

if choise==1:
    print("area= ",Geometry.circle_area(operand))

elif choise==2:
    print("circumference= ",Geometry.circle_circumference(operand))
    

elif choise==3:
    print("circumference= ",Geometry.square_root_check(operand))
    

else:
    print('Task finished!!')

