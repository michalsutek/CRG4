import turtle
kurz=1.2464

def eur2usd(suma_eur):
    """Prevod sumy penazi z EUR na doláre

    :param suma_eur: suma v EUR
    :type suma_eur: float
    :rtype suma_dolar: float
    
    """
    suma_dolar=kurz*suma_eur
    return suma_dolar

tabula = turtle.Screen()
eur=tabula.numinput("Eur","Zadajte sumu v EUR:")
dolar=eur2usd(eur)
pero=turtle.Turtle()
pero.penup()

pero.write("Suma v EUR:")
pero.forward(100)
pero.write(eur)
pero.right(90)
pero.forward(20)
pero.left(90)
pero.forward(-100)
pero.write("Suma v USD:")
pero.forward(100)
pero.write(dolar)

pero.hideturtle()        
tabula.mainloop()



        
