import datetime as dt
users = ['Shahid', 'Osama']
get_input = input("Enter Name: ")

def shahid():
    user_input = ''
    diet_input = ''
    print("1- Diet")
    print("2- Exercise")
    try:
        user_input = int(input())
    except ValueError as v:
        print("Invalid Entry...!!!")
    if user_input == 1:
        print("1- Load Data")
        print("2- Fetch Data")
        try:
            diet_input = int(input())
        except ValueError as v:
            print("Invalid Entry...!!!")
        if diet_input == 1:
            diet = input("Enter Diet: ")
            with open('Shahid_diet.txt', 'a') as write:
                d_time = dt.datetime.now()
                write.write(f"{diet}\t\t{d_time}\n")
            print("\nEntered Successfully...")
        elif diet_input == 2:
            try:
                with open('Shahid_diet.txt') as read:
                    print(read.read(), end='\n')
            except FileNotFoundError as not_found:
                print("Error!\tFile Not Found...!!!")
                exit()
        else:
            print("Invalid Number...!!!")
            exit()
    elif user_input == 2:
        print("1- Load Data")
        print("2- Fetch Data")
        try:
            exercise_input = int(input())
        except ValueError as v:
            print("Invalid Entry...!!!")
        if exercise_input == 1:
            exercise = input("Enter Exercise: ")
            with open('Shahid_exercise.txt', 'a') as write:
                d_time = dt.datetime.now()
                write.write(f"{exercise}\t\t{d_time}\n")
            print("\nEntered Successfully...")
        elif exercise_input == 2:
            try:
                with open('Shahid_exercise.txt') as read:
                    print(read.read(), end='\n')
            except FileNotFoundError as not_found:
                print("Error!\tFile Not Found...!!!")
                exit()
        else:
            print("Invalid Number...!!!")
            exit()
    else:
        print("Invalid Number...!!!")
        exit()

def osama():
    user_input = ''
    exercise_input = ''
    print("1- Diet")
    print("2- Exercise")
    try:
        user_input = int(input())
    except ValueError as v:
        print("Invalid Entry...!!!")
    if user_input == 1:
        print("1- Load Data")
        print("2- Fetch Data")
        try:
            diet_input = int(input())
        except ValueError as v:
            print("Invalid Entry...!!!")
        if diet_input == 1:
            diet = input("Enter Diet: ")
            with open('Osama_diet.txt', 'a') as write:
                d_time = dt.datetime.now()
                write.write(f"{diet}\t\t{d_time}\n")
            print("\nEntered Successfully...")
        elif diet_input == 2:
            try:
                with open('Osama_diet.txt') as read:
                    print(read.read(), end='\n')
            except FileNotFoundError as not_found:
                print("Error!\tFile Not Found...!!!")
                exit()
        else:
            print("Inavlid Entry...!!!")
            exit()
    elif user_input == 2:
        print("1- Load Data")
        print("2- Fetch Data")
        try:
            exercise_input = int(input())
        except ValueError as v:
            print("Invalid Entry...!!!")
        if exercise_input == 1:
            exercise = input("Enter Exercise: ")
            with open('Osama_exercise.txt', 'a') as write:
                d_time = dt.datetime.now()
                write.write(f"{exercise}\t\t{d_time}\n")
            print("\nEntered Successfully...")
        elif exercise_input == 2:
            try:
                with open('Osama_exercise.txt') as read:
                    print(read.read(), end='\n')
            except FileNotFoundError as not_found:
                print("Error!\tFile Not Found...!!!")
                exit()
        else:
            print("Invalid Number...!!!")
            exit()
    else:
        print("Invalid Entry...!!!")
        exit()

if get_input.capitalize() not in users:
    print("User is not Specified...!!!")

elif get_input.capitalize() == 'Shahid':
    shahid()

elif get_input.capitalize() == 'Osama':
    osama()
exit()
