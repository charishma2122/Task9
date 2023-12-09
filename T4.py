import re
def validate_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(regex, email))
def validate_bangladesh_mobile_number(number):
    regex = r'^\+?(880)?1[3-9]\d{8}$'
    return bool(re.match(regex, number))
def validate_usa_telephone_number(number):
    regex = r'^\+?1?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'
    return bool(re.match(regex, number))
def validate_alpha_numeric_password(password):
    regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$'
    return bool(re.match(regex, password))
def validate_user_inputs():
    email = input("Enter an email address: ")
    if validate_email(email):
        print("Valid email!")
    else:
        print("Invalid email!")

    mobile_number = input("Enter a Bangladesh mobile number with country code (+880): ")
    if validate_bangladesh_mobile_number(mobile_number):
        print("Valid Bangladeshi mobile number!")
    else:
        print("Invalid Bangladeshi mobile number!")

    us_telephone = input("Enter a USA telephone number with country code (+1): ")
    if validate_usa_telephone_number(us_telephone):
        print("Valid USA telephone number!")
    else:
        print("Invalid USA telephone number!")

    password = input("Enter a 16-character alpha-numeric password: ")
    if validate_alpha_numeric_password(password):
        print("Valid password!")
    else:
        print("Invalid password!")

validate_user_inputs()
