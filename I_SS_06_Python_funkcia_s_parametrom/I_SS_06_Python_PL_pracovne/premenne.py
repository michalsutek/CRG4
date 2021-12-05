import turtle
tabula=turtle.Screen()
pero=turtle.Turtle()

strana=20

def trojuholnik():
    for i in range(3):
        pero.forward(strana)
        pero.right(120)

def stvoruholnik():
    for i in range(4):
        pero.forward(strana)
        pero.right(90)    

trojuholnik()
pero.penup()
pero.forward(2*strana)
pero.pendown()
stvoruholnik()

pero.hideturtle()
tabula.mainloop()

