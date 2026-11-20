# password validator

def validate_password(password):
    has_upper= False
    has_digit= False
    has_specialChar= False

    specialCharacters= '`~!@#$%^&*()-_+=[]}{|.,><?/'

    for char in password:
        if char.isupper():
            has_upper=True

        elif char.isdigit():
            has_digit=True

        elif char in specialCharacters:
            has_specialChar= True

    if len(password)>=8:
        if has_upper==True:
            if has_digit==True:
                if has_specialChar== True:
                    return True
    else:
        return False
    
def check_Strength(password):
    if validate_password(password)==True:
        return 'Strong'
    
    else:
        return 'Weak'

        
        