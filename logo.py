import turtle
from turtle import *

t=turtle.Turtle()
wn=Screen()

wn.bgcolor("#800000")
t.pensize(1)
t.hideturtle()

#circles
t.penup()
t.setposition(0,-270)
t.pendown()
t.begin_fill()
t.color("#ffc300")
t.pencolor("#ffc300")
t.circle(270)
t.end_fill()
t.penup()

t.setposition(0,-240)
t.pendown()
t.begin_fill()
t.color("black")
t.pencolor("black")
t.circle(240)
t.end_fill()
t.penup()

t.setposition(240,0)
t.pendown()
t.begin_fill()
t.color("#4d0000")
t.pencolor("#4d0000")
t.fd(30)
t.right(-90)
t.circle(270,90)
t.right(270)
t.fd(30)
t.right(90)
t.circle(240,-90)
t.end_fill()
t.penup()

t.setposition(190,-194)
t.pendown()
t.begin_fill()
t.color("#ff0000")
t.pencolor("#ff0000")
t.right(140)
t.fd(30)
t.right(-94)
t.circle(300,200)
t.right(-90)
t.fd(30)
t.right(90)
t.circle(269,-200)
t.end_fill()
t.penup()

t.setposition(-30,298)
t.pendown()
t.begin_fill()
t.color("#330000")
t.pencolor("#330000")
t.right(218)
t.circle(300,235)
t.right(90)
t.fd(30)
t.right(270)
t.circle(330,-235)
t.right(-90)
t.fd(30)
t.end_fill()
t.penup()

#face upper part
t.setposition(0,140)
t.pendown()
t.begin_fill()
t.color("#ffbf00")

p1=[(-30,140),(-60,220),(-110,200),(-140,180),(-140,110),(-130,60),(-150,30),(-130,
    10),(-115,30),(-30,0),(10,0),(10,0),(30,0),(120,30),(130,5),(150,25),(140,55),
    (150,110),(150,170),(110,200),(60,220),(30,140),(0,140)]

for pos in p1:
    x,y=pos
    t.setposition(x,y)
t.end_fill()
t.penup()

#face middle part
t.setposition(0,-10)
t.pendown()
t.begin_fill()
t.color("#ffbf00")

p2=[(-30,-10),(-40,-20),(-80,-25),(-110,-18),(-154,25),(-170,-5),(-170,-20),(-100,
    -140),(-90,-170),(-60,-190),(-46,-170),(0,-170),(0,-170),(54,-170),(65,-190),
    (98,-170),(105,-140),(177,-20),(177,-5),(156,20),(102,-25),(78,-30),(40,-23),
    (30,-10),(0,-10)]

for pos in p2:
    x,y=pos
    t.setposition(x,y)
t.end_fill()
t.penup()

#face lower part
t.setposition(0,-180)
t.pendown()
t.begin_fill()
t.color("#ffbf00")

p3=[(-40,-180),(-60,-204),(-90,-182),(-100,-200),(-65,-230),(-40,-215),(-20,-215),
    (-10,-205),(0,-205),(20,-205),(30,-215),(50,-215),(75,-228),(110,-198),(100,
    -180),(66,-202),(48,-180),(0,-180)]

for pos in p3:
    x,y=pos
    t.setposition(x,y)
t.end_fill()

turtle.done()