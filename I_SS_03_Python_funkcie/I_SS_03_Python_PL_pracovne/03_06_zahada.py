import turtle

def obrazok():
    pero.forward(100)
    pero.left(120)
    pero.forward(200)
    pero.left(-120)
    pero.forward(100)
    pero.left(-120)
    pero.forward(200)
    pero.left(120)


tabula = turtle.Screen()
pero = turtle.Turtle()
pero.pensize(10)
pero.pencolor("green")
pero.fillcolor("yellow")

pero.begin_fill()
obrazok()
pero.end_fill()

tabula.mainloop()

