import turtle             # rozšírenie Pythonu o príkazy korytnačej grafiky

pero = turtle.Turtle()    # vytvorí sa grafické pero s menom "pero"
tabula = turtle.Screen()  # vytvorí sa grafická plocha s menom "tabula"
tabula.bgcolor("lightyellow")

pero.forward(100)
pero.left(45)
pero.forward(-20)
pero.forward(20)
pero.left(-90)
pero.forward(-20)
pero.forward(20)
pero.left(45)
pero.forward(-100)

tabula.mainloop()         # ponechá otvorené okno s grafickou plochou
