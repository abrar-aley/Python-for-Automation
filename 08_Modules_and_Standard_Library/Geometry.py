import math

def circle_area(radius):
    return math.pi*math.pow(radius,2)

def circle_circumference(radius):
    return 2*math.pi*radius

def square_root_check(num):
    return math.sqrt(num)

def default():
    print("This is geometry module by abrar ali")

if __name__=="__main__":
    default();

