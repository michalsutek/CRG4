import turtle
tabula = turtle.Screen()
pero = turtle.Turtle()
pero.width(2)
pero.penup()

cislo_1=tabula.numinput("Vstup", "Zadaj prvé číslo:")
cislo_2=tabula.numinput("Vstup", "Zadaj druhé číslo:")
if cislo_1>cislo_2:
    pero.write("Väčšie je číslo:")
    pero.forward(100)
    pero.write(cislo_1)
elif cislo_2>cislo_1:
    pero.write("Väčšie je číslo:")
    pero.forward(100)
    pero.write(cislo_2)
else:
    pero.write("Čísla sú rovnaké!")
    

tabula.mainloop()
