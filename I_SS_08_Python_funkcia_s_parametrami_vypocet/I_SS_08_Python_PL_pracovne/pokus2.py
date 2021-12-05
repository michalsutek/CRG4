import turtle
tabula = turtle.Screen()
a=tabula.numinput("Číslo", "Zadaj prvé číslo:")

pero=turtle.Turtle()

pero.right(90)
pero.penup()
for i in range(5):
    pero.forward(50)
    pero.write(a+8)
        
tabula.mainloop()



        
