from turtle import *
import random
from turtle import TurtleGraphicsError
while True:
    colorSelect = input("Color (rainbow): ")
    if (colorSelect == "rainbow") or (colorSelect == ''):
        colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        print("Rainbow Selected! :)")
        crazy = input("Crazy rainbow? (y/n): ")
        if (crazy != "n") and (crazy != "y"):
            crazy = "n"
    elif (colorSelect != "rainbow") and (colorSelect != ''):
        colors = [str(colorSelect)]
        print(str(colorSelect) + " chosen. :)")
        crazy = "n"
    speedSelect = input("Speed (1-10): ")
    if (speedSelect == '1') or (speedSelect == '2') or (speedSelect == '3') or (speedSelect == '4') or (speedSelect == '5') or (speedSelect == '6') or (speedSelect == '7') or (speedSelect == '8') or (speedSelect == '9') or (speedSelect == '10'):
        speed(int(speedSelect))
    else:
        speed(2)
    
    try: pencolor(colorSelect)
    except TurtleGraphicsError: colorSelect = "INVALID"
    if (colorSelect != "INVALID"):
        bgcolor("black")
        width(5)
        if (crazy == "n"):
            for y in range(90):
                color = random.randint(0, len(colors)-1)
                pencolor(colors[color])
                a = random.randint(-400, 400)
                b = random.randint(-400, 400)
                c = random.randint(0, 90)
                penup()
                goto(a, b)
                pendown()
                right(c)
                for x in range(12):
                    forward(5)
                    right(1)
                for x in range(18):
                    forward(2)
                    right(6)
                for x in range(13):
                    forward(3)
                    right(8)
                left(170)
                for x in range(10):
                    forward(3)
                    right(7)
                for x in range(22):
                    forward(2)
                    right(6)
                for x in range(13):
                    forward(5)
                    right(1)

        elif (crazy == 'y'):
            for y in range(90):
                color = random.randint(0, len(colors)-1)
                pencolor(colors[color])
                a = random.randint(-350, 350)
                b = random.randint(-350, 350)
                c = random.randint(0, 90)
                penup()
                goto(a, b)
                pendown()
                right(c)
                for x in range(12):
                    color = random.randint(0, len(colors)-1)
                    pencolor(colors[color])
                    forward(5)
                    right(1)
                for x in range(18):
                    color = random.randint(0, len(colors)-1)
                    pencolor(colors[color])
                    forward(2)
                    right(6)
                for x in range(13):
                    color = random.randint(0, len(colors)-1)
                    pencolor(colors[color])
                    forward(3)
                    right(8)
                left(170)
                for x in range(10):
                    color = random.randint(0, len(colors)-1)
                    pencolor(colors[color])
                    forward(3)
                    right(7)
                for x in range(22):
                    color = random.randint(0, len(colors)-1)
                    pencolor(colors[color])
                    forward(2)
                    right(6)
                for x in range(13):
                    color = random.randint(0, len(colors)-1)
                    pencolor(colors[color])
                    forward(5)
                    right(1)
        hideturtle()
        done()
    else:
        print("Ivalid color. Please try again")
