'''
This Program is to Validate email address i.e, entered email formate is valid or not
'''
# importing re (Regular expression) module
import re

# Make a regular expression
condition_check = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

user_email = input('Enter user email ID : ')
# Condition check for validation
if re.search(condition_check, user_email):
    print('Your Email is Valid.')
else:
    print('Entered an Invalid Email.')
exit()
