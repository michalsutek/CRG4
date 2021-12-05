import turtle
tabula = turtle.Screen()
pero = turtle.Turtle()
pero.width(2)
pero.penup()

heslo=tabula.textinput("Test vstupu", "Zadaj heslo:")
if heslo=="pyton":
    pero.write("Zadal si správne heslo!")
else:
    pero.write("Zadal si nesprávne heslo!")
    

tabula.mainloop()
