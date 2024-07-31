from turtle import Turtle
from turtle import Screen
import random
def turn(sides):
    colorslist=["red","blue","black"]
    angle=360//sides;
    thanuj.color(random.choice(colorslist))
    for i in range(0,sides):
        thanuj.forward(100)
        thanuj.right(angle)

def random_walk():
    angleslist=[90,180,270,0]
    colorslist = ["red", "blue", "black"]
    thanuj.pensize(10)
    thanuj.color(random.choice(colorslist))
    thanuj.forward(10)
    thanuj.setheading(random.choice(angleslist))

def shape_of_all():
    for i in range(3,9):
        turn(i)

def dashed_line():
    for i in range(0, 4):
        thanuj.forward(10)
        thanuj.penup()
        thanuj.forward(10)
        thanuj.pendown()
def spirograph(sizes):
    for i in range(360 // sizes):
        thanuj.circle(30)
        thanuj.setheading(thanuj.heading() + sizes)

#scr=Screen()
#thanuj=Turtle()

#thanuj.shape("turtle")
#thanuj.color("blue")
#turn(5) this is only one if you want all different sides then you have to give the loops
#shape_of_all()
#dashed_line()
#random_walk()
#spirograph(60)

#scr.exitonclick()

colorslist = ["red", "blue", "green", "yellow", "orange", "purple", "cyan", "magenta"]

thanuj=Turtle()
sc=Screen()
for j in range (0,5):
    for i in range(0,10):
        thanuj.dot(20,random.choice(colorslist))
        thanuj.penup()
        thanuj.forward(30)
        thanuj.pendown()
    thanuj.left(90)
    thanuj.penup()
    thanuj.forward(30)
    thanuj.pendown()
    thanuj.left(90)
    for i in range(0,10):
        thanuj.penup()
        thanuj.forward(30)
        thanuj.pendown()
        thanuj.dot(20,random.choice(colorslist))
    thanuj.right(90)
    thanuj.penup()
    thanuj.forward(30)
    thanuj.pendown()
    thanuj.right(90)
sc.exitonclick()