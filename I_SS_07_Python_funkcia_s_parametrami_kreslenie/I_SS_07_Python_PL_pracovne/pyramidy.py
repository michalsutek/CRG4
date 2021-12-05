import turtle
tabula = turtle.Screen()
pero = turtle.Turtle()
pero.width(2)

def poschodie(velkost):
    pero.color("brown")
    pero.begin_fill()
    for i in range(2):
        pero.forward(velkost)
        pero.left(90)
        pero.forward(20)
        pero.left(90)
    pero.end_fill()

def pyramida(pocet_poschodi):
    zakladna_velkost=50
    for i in range(pocet_poschodi):
        poschodie(zakladna_velkost)
        pero.penup()
        pero.right(90)
        pero.forward(20)
        pero.left(90)
        pero.backward(20)
        pero.pendown()
        zakladna_velkost=zakladna_velkost+40
        

pyramida(5)
pero.hideturtle()
tabula.mainloop()


