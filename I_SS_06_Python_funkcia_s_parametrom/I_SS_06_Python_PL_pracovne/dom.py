import turtle
tabula = turtle.Screen()
pero = turtle.Turtle()
pero.width(2)

def okno():
    # definovanie vykreslovania okna
    pero.pendown()
    pero.color("skyblue")
    pero.begin_fill()
    for i in range(4):
        pero.forward(50)
        pero.left(90)
    pero.end_fill()
    pero.penup()
    
def dom():
    # definovanie vykreslovania celeho domu
    pero.pendown()
    pero.color("orange")
    pero.begin_fill()
    for i in range(4):
        pero.forward(200)
        pero.left(90)
    pero.end_fill()
    pero.penup()
    pero.left(90)
    pero.forward(200)
    pero.color("red")
    pero.begin_fill()
    pero.right(90)
    for i in range(3):
        pero.forward(200)
        pero.left(120)
    pero.end_fill()
    pero.forward(25)
    pero.right(90)
    pero.forward(100)
    pero.left(90)
    okno()
    pero.forward(100)
    okno()
    
dom()   # vykreslenie domu
pero.hideturtle()
tabula.mainloop()
