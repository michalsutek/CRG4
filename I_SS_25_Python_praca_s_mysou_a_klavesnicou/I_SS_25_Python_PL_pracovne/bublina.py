import tkinter

velkost=20

def posun_bublinu(udalost):
    klaves=udalost.keysym
    if klaves=="Left":
        platno.move(bublina_1,-10,0)
        
okno=tkinter.Tk()
okno.title("Bublina")    
platno=tkinter.Canvas(okno, height=300, width=300, bg="lightgray")
platno.pack()
bublina_1=platno.create_oval(150-velkost/2,150-velkost/2,150+velkost/2, 150+velkost/2,fill="red")
platno.bind_all("<Key>",posun_bublinu)
okno.mainloop()

