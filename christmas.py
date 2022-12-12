from turtle import *
from random import randint


def create_rectangle(turtle, color, x, y, width, height):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()

    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)

    # fill the above shape
    turtle.end_fill()
    # Reset the orientation of the turtle
    turtle.setheading(0)




BG_COLOR = "#172A3A"

image = Turtle()
# set turtle speed
image.speed(2)
screen = image.getscreen()
# set background color
screen.bgcolor(BG_COLOR)
# set tile of screen
screen.title("Merry Christmas!")
# maximize the screen
screen.setup(width=1.0, height=1.0)

y = -100
# create tree trunk
create_rectangle(image, "red", -15, y-60, 30, 60)

# create tree
width = 240
image.speed(10)
while width > 10:
    width = width - 10
    height = 10
    x = 0 - width/2
    create_rectangle(image, "green", x, y, width, height)
    y = y + height

# create a star a top of tree
image.speed(1)
image.penup()
image.color('Gold')
image.goto(-20, y+10)
image.begin_fill()
image.pendown()
for i in range(5):
    image.forward(40)
    image.right(144)
image.end_fill()

tree_height = y + 40

# now add few stars in sky
image.speed(10)
number_of_stars = randint(20,30)
# print(number_of_stars)
for _ in range(0,number_of_stars):
    x_star = randint(-(screen.window_width()//2),screen.window_width()//2)
    y_star = randint(tree_height, screen.window_height()//2)
    size = randint(5,20)
    image.penup()
    image.color('gold')
    image.goto(x_star, y_star)
    image.begin_fill()
    image.pendown()
    for i in range(5):
        image.forward(size)
        image.right(144)
    image.end_fill()

# print greeting message
image.speed(1)
image.penup()
msg = "Merry Christmas, enter name!"
image.goto(0, -250)  # y is in minus because tree trunk was below x axis
image.color("Gold")
image.pendown()
image.write(msg, move=False, align="center", font=("Arial",30 , "bold"))

image.hideturtle()
screen.mainloop()