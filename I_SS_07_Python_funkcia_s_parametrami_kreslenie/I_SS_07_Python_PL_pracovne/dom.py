import turtle
tabula = turtle.Screen()
pero = turtle.Turtle()
pero.width(2)

def okno(velkost_okna):
    pero.pendown()
    pero.color("skyblue")
    pero.begin_fill()
    for i in range(4):
        pero.forward(velkost_okna)
        pero.left(90)
    pero.end_fill()
    pero.penup()
    
def dom(velkost):
    pero.pendown()
    pero.color("orange")
    pero.begin_fill()
    for i in range(4):
        pero.forward(velkost)
        pero.left(90)
    pero.end_fill()
    pero.penup()
    pero.left(90)
    pero.forward(velkost)
    pero.color("red")
    pero.begin_fill()
    pero.right(90)
    for i in range(3):
        pero.forward(velkost)
        pero.left(120)
    pero.end_fill()
    pero.forward(velkost/8)
    pero.right(90)
    pero.forward(velkost/2)
    pero.left(90)
    okno(velkost/4)
    pero.forward(velkost/2)
    okno(velkost/4)
dom(200)
pero.hideturtle()
tabula.mainloop()
