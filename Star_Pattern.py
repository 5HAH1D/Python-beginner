'''
This Simple Program is to print stars in triangular pattern by taking no_of_rows from the user.
'''
user_input = int(input("Enter number of rows: "))
print("1 for Ascending order\n0 for Descending order \n")
path = bool(int(input("Enter 1 or 0: ")))
if path:
    for i in range(1, user_input+1):
        print(i * "*")
else:
    for i in range(user_input, 0, -1):
        print(i * "*")
exit()

