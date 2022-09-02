'''
This simple program is to check weather entered input is a Numeric value or not.
'''
check = input("Enter anything: ")
if check.isnumeric():
    print("Numeric value")
else:
    print("Not a numeric")