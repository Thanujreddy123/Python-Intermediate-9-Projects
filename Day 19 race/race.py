import turtle
from turtle import Turtle
from turtle import Screen
import random
thanuj=Turtle("turtle")
scr=Screen()

is_race_on=False

userinput=scr.textinput("what is the colour of user who will win","write a name")
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
coordinate=[-100,-50,0,50,100,150]
turtlelist=[]
for i in range(6):
    tim=Turtle("turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(-210,coordinate[i])
    tim.pendown()
    turtlelist.append(tim)

thanuj.hideturtle()
if userinput:
    is_race_on=True
while is_race_on:
    for i in turtlelist:
        distance = random.randint(0, 20)
        i.penup()
        i.forward(distance)
        i.pendown()
        if i.xcor()>230:
            winning_color=i.pencolor()
            if winning_color==userinput:
                print(f"you won the {winning_color}")
            else:
                print("you have lost")
            is_race_on=False
            break



scr.exitonclick()