first_val = int(input("Enter your 1st value: "))
x = input("Enter operator: ")
second_val = int(input("Enter your 2nd value: "))

if x == '*':
    first_val += 5
    print("Result is : ", first_val * second_val)
elif x == '/':
    first_val += 15
    print("Result is : ", first_val / second_val)
elif x == '+':
    first_val += 19
    print("Result is : ", first_val + second_val)
elif x == '-':
    first_val += 9
    print("Result is : ", first_val - second_val)
elif x == '%':
    print("Result is : ", first_val % second_val)
else:
    print("Enter a valid input..!")
exit()
