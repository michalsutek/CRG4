import turtle
tabula = turtle.Screen()
pero = turtle.Turtle()



def slnko(pocet,farba):
   pero.pencolor(farba)
   for i in range(pocet):
      pero.forward(100)
      pero.forward(-100)
      pero.left(360 / pocet)
   pero.dot(100,farba)

def schod():
   pero.left(90)
   pero.forward(30)
   pero.right(90)
   pero.forward(30)

def schody(pocet):
   for i in range(pocet):
      schod()

schody(3)

tabula.mainloop()