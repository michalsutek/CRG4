import turtle

def vypocetBMI(hmotnost,vyska):
    """Vypocitanie BMI pre osobu s danou hmotnostou a vyskou

    :param hmotnost: hmotnost v kg
    :type hmotnost: float
    :param vyska: vyska v m
    :type vyska: float
    :rtype bmi: float
    
    """
    bmi=hmotnost/(vyska*vyska)
    return bmi

tabula = turtle.Screen()
m=tabula.numinput("Hmotnosť","Zadajte hmotnosť v kg:")
v=tabula.numinput("Výška","Zadajte výšku v m:")
vysledok=vypocetBMI(m,v)

pero=turtle.Turtle()
pero.penup()

pero.write("Hmotnost v kg:")
pero.forward(150)
pero.write(m)
pero.right(90)
pero.forward(20)
pero.left(90)
pero.forward(-150)
pero.write("Výška v m:")
pero.forward(150)
pero.write(v)
pero.right(90)
pero.forward(20)
pero.left(90)
pero.forward(-150)
pero.write("Body Mass Index:")
pero.forward(150)
pero.write(vysledok)

pero.hideturtle()        
tabula.mainloop()




        
