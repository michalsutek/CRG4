import turtle

#Funkcie na zobrazovanie na disleji
def pozadie():
    """Vykreslenie prazdneho displeja"""
    pero.color("black")
    pero.begin_fill()
    for i in range(2):
        pero.forward(50)
        pero.right(90)
        pero.forward(100)
        pero.right(90)
    pero.end_fill()
    pero.forward(5)
    pero.right(90)
    pero.forward(5)
    pero.color("gray")
    pero.pendown()
    pero.forward(40)
    pero.penup()
    pero.forward(10)
    pero.pendown()
    pero.forward(40)
    pero.left(90)
    pero.forward(40)
    pero.left(90)
    pero.forward(40)
    pero.penup()
    pero.forward(5)
    pero.pendown()
    pero.left(90)
    pero.forward(40)
    pero.penup()
    pero.backward(40)
    pero.right(90)
    pero.forward(5)
    pero.pendown()
    pero.forward(40)
    pero.left(90)
    pero.forward(40)
    pero.left(90)
    pero.penup()
    
def nula():
    """Zobrazenie cisla 0 na displeji"""
    pozadie()
    pero.color("red")
    pero.pendown()
    pero.forward(40)
    pero.penup()
    pero.forward(10)
    pero.pendown()
    pero.forward(40)
    pero.left(90)
    pero.forward(40)
    pero.left(90)
    pero.forward(40)
    pero.penup()
    pero.forward(10)
    pero.pendown()
    pero.forward(40)
    pero.left(90)
    pero.forward(40)
    pero.left(90)
    pero.penup()

def jeden():
    """Zobrazenie cisla 1 na displeji"""
    pozadie()
    pero.color("red")
    pero.left(90)
    pero.forward(40)
    pero.right(90)
    pero.pendown()
    pero.forward(40)
    pero.penup()
    pero.forward(10)
    pero.pendown()
    pero.forward(40)
    pero.penup()
    pero.right(90)
    pero.forward(40)
    pero.right(90)
    pero.forward(90)
    pero.left(180)

def dva():
    """Zobrazenie cisla 2 na displeji"""
    pozadie()
    pero.color("red")
    pero.forward(90)
    pero.left(90)
    pero.forward(40)
    pero.pendown()
    pero.backward(40)
    pero.left(90)
    pero.forward(40)
    pero.penup()
    pero.forward(5)
    pero.right(90)
    pero.pendown()
    pero.forward(40)
    pero.penup()
    pero.left(90)
    pero.forward(5)
    pero.pendown()
    pero.forward(40)
    pero.left(90)
    pero.forward(40)
    pero.penup()
    pero.left(90)

def tri():
    """Zobrazenie cisla 3 na displeji"""
    pozadie()
    pero.color("red")
    pero.forward(90)
    pero.left(90)
    pero.pendown()
    pero.forward(40)
    pero.left(90)
    pero.forward(40)
    pero.penup()
    pero.forward(5)
    pero.left(90)
    pero.pendown()
    pero.forward(40)
    pero.penup()
    pero.backward(40)
    pero.right(90)
    pero.forward(5)
    pero.pendown()
    pero.forward(40)
    pero.left(90)
    pero.forward(40)
    pero.left(90)
    pero.penup()

tabula = turtle.Screen()
pero = turtle.Turtle()
pero.width(4)
pero.penup()

#Tu vlozte svoj kod
    

pero.hideturtle()
tabula.mainloop()
