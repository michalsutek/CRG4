import turtle

def vzor():
    # definovanie vykreslenia vzoru
    pero.dot(50, "black")
    pero.forward(50)
    pero.dot(50, "lightgray")
    pero.forward(50)


tabula = turtle.Screen()
pero = turtle.Turtle()
pero.penup()

vzor()          # vykreslenie vzoru
pero.right(90)  # otocenie sa o 90 stupnov vpravo
vzor()          # vykreslenie vzoru

tabula.mainloop()

