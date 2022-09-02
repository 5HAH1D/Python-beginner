'''
This Program Generates Random Password by Taking Password length from the user.
'''
import random
import string
# characters to generate password from
password_characters = list(string.ascii_letters + string.digits + string.punctuation)


def generate_password():
    # Taking Input from the User
    Password_length = input("Enter length of Your Password: ")
    if Password_length.isnumeric():
        # shuffling the characters
        random.shuffle(password_characters)

        password = []
        for i in range(int(Password_length)):
            password.append(random.choice(password_characters))

        # Again Shuffling Characters
        random.shuffle(password)
        print("".join(password))
    else:
        print("Invalid Entry...Try a Number.")
        generate_password()


generate_password()
exit()
