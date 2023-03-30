from tkinter import *

# A global variable to store the result of the calculation
global result_value


def on_click(event):
    """
    Callback function for button click events.
    Takes an event object and updates the screen based on the button clicked.
    """
    global screen_value
    # Get the value of the button that was clicked
    value = event.widget.cget("text")

    if value == '=':
        # If the equals button was clicked, evaluate the expression on the screen and display the result
        global result_value

        # If the expression on the screen contains only digits, set the result to the integer value of the expression
        if screen_value.get().isdigit():
            result_value = int(screen_value.get())
        # If the expression contains any other characters, evaluate it as a mathematical expression
        else:
            try:
                result_value = eval(screen_value.get())
            except Exception as error:
                # If there is an error in the expression, set the result to "ERROR"
                print(error)
                result_value = "ERROR"
            finally:
                # Set the screen value to the result and update the screen
                screen_value.set(result_value)
                screen.update()

    elif value == 'C':
        # If the C button was clicked, clear the screen
        screen_value.set("")
        screen.update()

    elif value == 'Del':
        # If the Del button was clicked, delete the last character on the screen
        sc_value = str(screen_value.get())
        sc_value = sc_value[:-1]
        screen_value.set(sc_value)
        screen.update()

    else:
        # If any other button was clicked, add its value to the screen
        screen_value.set(screen_value.get() + value)
        screen.update()


if __name__ == '__main__':
    root = Tk()
    root.geometry('315x360')
    root.title('Calculator')
    # you can add your icon here (file extension should be .ico)
    # root.wm_iconbitmap('<path>/icon.ico')

    # List of buttons to display on the calculator
    text_list = ['C', '/', '%', 'Del', '9', '8', '7', '+', '6', '5', '4', '-', '3', '2', '1', '*', '00', '0', '.', '=']

    # A variable to store the value displayed on the calculator screen
    screen_value = StringVar()
    screen_value.set("")

    # Create a text entry widget for the calculator screen
    screen = Entry(root, textvariable=screen_value, font='consolas 46', borderwidth='2px', bg='sky blue')
    screen.pack(side=TOP, fill=X)

    item = 0
    for i in range(5):
        f = Frame(root)
        for j in range(4):
            # Create a button for each item in the text_list
            button = Button(f, text=text_list[item], font='arial 20 bold', width=4)
            button.pack(side=LEFT)
            button.bind("<Button-1>", on_click)
            item += 1
        f.pack()

    root.mainloop()
