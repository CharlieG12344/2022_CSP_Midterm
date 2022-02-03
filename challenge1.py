'''
Write a turtle program that draws 10 parrallel lines.
* Must use a loop - cannot use 10 turtle draw commands
Each parallel line should be a randomly selected color and randomly selected length.
* Color should be selected randomly from a list
* The length of each line should be generated randomly (you may choose your own method).

Don't forget your imports!!!
'''

import turtle as trtl
import random as rand
painter = trtl.Turtle()
painter.hideturtle()
colors = ["red", "blue", "green", "yellow", "black", "gray", "purple", "pink", "magenta", "teal"]

def lines(painter):
    y = 100
    x = 0
    while x <= 9:
        choice = rand.choice(colors)
        length = rand.randint(0, 750)
        painter.penup()
        painter.goto(-300,y)
        painter.pencolor(choice)
        painter.pendown()
        painter.forward(length)
        y -= 10
        x += 1

lines(painter)


wn = trtl.Screen()
wn.mainloop()