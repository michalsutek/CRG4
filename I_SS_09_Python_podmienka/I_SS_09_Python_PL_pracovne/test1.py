import turtle
tabula = turtle.Screen()
pero = turtle.Turtle()
pero.width(2)
pero.penup()

for i in range(10):
    pero.write(i)
    pero.forward(10)
    if i==5:
        pero.write("*")
        pero.forward(20)
    

tabula.mainloop()
