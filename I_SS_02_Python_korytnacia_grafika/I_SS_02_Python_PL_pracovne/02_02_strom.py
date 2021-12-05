import turtle             # rozšírenie Pythonu o príkazy korytnačej grafiky

pero = turtle.Turtle()    # vytvorí sa grafické pero s menom "pero"
tabula = turtle.Screen()  # vytvorí sa grafická plocha s menom "tabula"

pero.pensize(5)           # nastaví sa hrúbka pera na 5 bodov
pero.pencolor("brown")    # nastaví sa farba pera na hnedú
pero.forward(100)         # pero sa posunie o 100 bodov dopredu
pero.dot(100, "green")    # vykreslí zelený kruh s priemerom 100 bodov
pero.forward(-100)        # pero sa posunie o 100 bodov vzad

tabula.mainloop()         # ponechá otvorené okno s grafickou plochou
