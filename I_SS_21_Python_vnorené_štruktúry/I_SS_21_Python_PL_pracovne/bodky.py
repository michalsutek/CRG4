import turtle 
import random

pero=turtle.Turtle()
tabula=turtle.Screen()
pero.speed(0)
pero.hideturtle()
pero.penup()

for i in range(250):
    x=random.randint(-100,100)
    y=random.randint(-100,100)
    if x<0:
        pero.color("red")
    else:
        pero.color("blue")
    pero.setposition(x,y)
    pero.dot(10)


tabula.mainloop()
