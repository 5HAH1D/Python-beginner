'''
This program is a simple Number_Guessing game take numbers from user,
matches with right Number and work accordingly.
'''
Number = 13
No_of_Turns = 5
print("\n     ----------Welcome to Number Guessing Game----------")
print("\nYou have 5 Turns to guess the Number...!!!\n")
print("Hint- Number is between 1 - 20.")
# Try blocks exists to deal with valueError if occurs
try:
    user_input = int(input("Enter Number: "))
    Turns_Left = No_of_Turns - 1
    while Turns_Left >= 0:
        if user_input == Number:
            print("\nCongratulations.....YOU WON__!!\n")
            print("You Won the Game in " + str(No_of_Turns - Turns_Left) + " Turn(s)...")
            break
        elif Turns_Left == 0:
            print("\nYou are out of Turns...!!!   Turns Left : ", Turns_Left)
            print("You Lost...!!!")
            break
        elif user_input < Number:
            print("Wrong Number.....No of Turns left: ", Turns_Left)
            Turns_Left -= 1
            user_input = int(input("Try a higher Number: "))
        elif user_input > Number:
            print("Wrong Number.....No of Turns left: ", Turns_Left)
            Turns_Left -= 1
            user_input = int(input("Try a smaller Number: "))
except ValueError as e:
    print("Invalid Value...!!! Try a Numeric Value. ")
exit()
