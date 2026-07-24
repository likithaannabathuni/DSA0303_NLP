import re

# Input
email = input("Enter Email: ")
password = input("Enter Password: ")
mobile = input("Enter Mobile Number: ")

# Regular Expressions
email_pattern = r'^[A-Za-z][A-Za-z0-9._]*@[A-Za-z]+\.(com|org|edu|net|in)$'
password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%&!]).{8,}$'
mobile_pattern = r'^[6-9]\d{9}$'

# Email Validation
if re.fullmatch(email_pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")

# Password Validation
if re.fullmatch(password_pattern, password):
    print("Strong Password")
else:
    print("Weak Password")

# Mobile Number Validation
if re.fullmatch(mobile_pattern, mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")
