import turtle

def stvorec(strana):
    """Vykreslovanie jedneho stvorca danej velkosti

    :param strana: velkost jedneho stvorca
    :type strana: int

    """
    for i in range(4):
        pero.forward(strana)
        pero.right(90)

def obrazec(pocet, velkost):
    """Vykreslovanie obrazca s danym poctom stvorcov danej pociatocnej velkosti

    :param pocet: pocet ciernobielych dvojic stvorcov 
    :type pocet: int
    :param velkost: pociatocna velkost jedneho stvorca
    :type velkost: int

    """    
    for i in range(pocet):
        pero.color("black")
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
        
tabula = turtle.Screen()
pero=turtle.Turtle()
pero.speed(0)

obrazec(20,200)
tabula.mainloop()

        
