from turtle import *
from random import *

farby=["red","green","blue"]
tabula=Screen()
pero=Turtle()
pero.speed(0)
pero.hideturtle()
for i in range(1000):
    farba=choice(farby)
    pero.color(farba)
    pero.forward(5)
    otocka=90*randint(0,3)
    pero.left(otocka)
print("KONIEC")
tabula.mainloop()
    
