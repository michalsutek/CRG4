import turtle
tabula = turtle.Screen()
farba_dosiek=tabula.textinput("FARBA", "Zadaj farbu po anglicky:")
pero=turtle.Turtle()
pero.speed(0)

def stvorec(strana):
    for i in range(4):
        pero.forward(strana)
        pero.right(90)

def obrazec(pocet, velkost,farba):
    for i in range(pocet):
        pero.color(farba)
        pero.begin_fill()
        stvorec(velkost)
        pero.end_fill()
        velkost=velkost-4
        pero.right(10)
        pero.color("white")
        pero.begin_fill()
        stvorec(velkost)
        pero.end_fill()
        velkost=velkost-4

obrazec(20,200, farba_dosiek)
tabula.mainloop()

        
