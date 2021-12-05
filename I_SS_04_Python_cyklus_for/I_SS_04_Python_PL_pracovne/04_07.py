import turtle

tabula = turtle.Screen()
pero = turtle.Turtle()

for i in range(5):
    pero.pendown()
    pero.forward(200)
    pero.forward(-200)
    pero.penup()
    pero.left(90)
    pero.forward(100 / 5)
    pero.left(-90)

tabula.mainloop()

