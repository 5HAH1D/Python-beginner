"""
This program allows the user to draw and save shapes using the turtle module.
The user can choose to draw a shape with a specified number of sides, size and color.
The program keeps track of all the shapes drawn by the user and allows the user to print
the names of all the shapes drawn.
"""


# Importing turtle module
import turtle

# Creating an empty list to store the names of shapes drawn
shapes = []


def draw_shape(_sides, _size, _color):
    """Draws a shape with the specified number of sides, size and color using the turtle module.
    Args:
        _sides (int): The number of sides of the shape to be drawn.
        _size (int): The size of the shape to be drawn.
        _color (str): The color of the shape to be drawn.
    Returns: None """
    # Set the color of the turtle to the specified color
    turtle.color(_color)
    turtle.fillcolor(_color)
    turtle.begin_fill()
    # Draw the shape with the specified number of sides and size
    for i in range(_sides):
        turtle.forward(_size)
        turtle.left(360/_sides)
    turtle.end_fill()
    # Make the turtle stay on the screen until user closes the window
    turtle.exitonclick()

    # Reset the turtle screen for the next drawing
    turtle.TurtleScreen._RUNNING = True


# Infinite loop to present options to the user until the program is ended
while True:
    print("Options:")
    print("1. Draw the shape.")
    print("2. Print the names of all the shapes already drawn.")
    print("0. End the program.")

    # Get the user's choice
    choice = int(input("Enter your choice: "))

    # Draw a shape with user-defined properties
    if choice == 1:
        shape_name = input("Enter a name for the shape: ")
        shapes.append(shape_name)
        sides = int(input("Enter the number of sides: "))
        size = int(input("Enter the size of the shape: "))
        color = input("Enter the color of the shape: ")

        # Move the turtle to the starting point and draw the shape
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        draw_shape(sides, size, color)

    # Print the names of all the shapes drawn
    elif choice == 2:
        print("Shapes drawn:")
        for shape in shapes:
            print(shape)

    # End the program
    elif choice == 0:
        break

    # Handle invalid input
    else:
        print("Invalid Choice!")
