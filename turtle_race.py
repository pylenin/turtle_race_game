import turtle
import random

turtle.title ('Turtle Race')
turtle.speed(10)
turtle.penup()
turtle.goto(-200,200)

for step in range(11):

    turtle.write(step)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(400)
    turtle.penup()
    turtle.backward(400)
    turtle.left(90)
    turtle.forward(40)
turtle.hideturtle()

d = {"t1":0, "t2":0, "t3":0}

t1 = turtle.Turtle()
t1.color('red')
t1.shape('turtle')
t1.penup()
t1.goto(-200,0)
t1.right(360)
t1.pendown()


t2 = turtle.Turtle()
t2.color('blue')
t2.shape('turtle')
t2.penup()
t2.goto(-200,50)
t2.left(360)
t2.pendown()

t3 = turtle.Turtle()
t3.color('green')
t3.shape('turtle')
t3.penup()
t3.goto(-200,-50)
t3.right(360)
t3.pendown()

while max(d.values()) <= 400:
    d1_next = random.randint(1,5)
    d2_next = random.randint(1,5)
    d3_next = random.randint(1, 5)
    t1.forward(d1_next)
    t2.forward(d2_next)
    t3.forward(d3_next)
    d['t1'] += d1_next
    d['t2'] += d2_next
    d['t3'] += d3_next

turtle.exitonclick()
print(d)



