from turtle import *
tabula=Screen()
pero=Turtle()
pero.hideturtle()

def kresli_krabicu(strana_a,strana_b,strana_c, farba):  #funkcia na vykreslenie krabice daných rozmerov a zadanej farby
    pero.color(farba)
    pero.begin_fill()
    for i in range(2):
        pero.left(45)
        pero.forward(strana_c)
        pero.left(45)
        pero.forward(strana_b)
        pero.left(90)
        pero.forward(strana_a)
    pero.end_fill()
    

kresli_krabicu(50,25,20,"blue")

tabula.mainloop()
