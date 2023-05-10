import turtle
shapes = []
def draw_shape(sides, size, color):
    turtle.color(color)
    for i in range(sides):
        turtle.forward(size)
        turtle.left(360/sides)

while True:
    print("Options:")
    print("1. Draw the shape.")
    print("2. Print the names of all the shapes already drawn.")
    print("0. End the program.")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        shape_name = input("Enter a name for the shape: ")
        shapes.append(shape_name)
        sides = int(input("Enter the number of sides: "))
        size = int(input("Enter the size of the shape: "))
        color = input("Enter the color of the shape: ")
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        draw_shape(sides, size, color)
    elif choice == 2:
        print("Shapes drawn:")
        for shape in shapes:
            print(shape)
    elif choice == 0:
        break
    else:
        print("Invalid Choice!")
turtle.exitonclick()