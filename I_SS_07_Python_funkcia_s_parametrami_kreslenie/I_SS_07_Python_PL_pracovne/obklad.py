import turtle
pero=turtle.Turtle()
pero.speed(0)

def stvorec(strana):
    for i in range(4):
        pero.forward(strana)
        pero.right(90)

def obkladacka(velkost):
    for i in range(10):
        pero.color("black")
        pero.begin_fill()
        stvorec(velkost)
        pero.end_fill()
        velkost=velkost-2
        pero.color("white")
        pero.begin_fill()
        stvorec(velkost)
        pero.end_fill()
        velkost=velkost-4
        

obkladacka(80)

        
