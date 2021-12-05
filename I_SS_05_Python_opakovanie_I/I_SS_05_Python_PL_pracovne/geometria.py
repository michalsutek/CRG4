import turtle
tabula = turtle.Screen()
pero = turtle.Turtle()
pero.width(2)

def sestuholnik():
    # definovanie vykreslenia sestuholnika
    pero.pendown()
    for i in range(6):
        pero.forward(20)
        pero.left(60)
    pero.penup()

    
sestuholnik()   # vykreslenie sestuholnika

tabula.mainloop()
