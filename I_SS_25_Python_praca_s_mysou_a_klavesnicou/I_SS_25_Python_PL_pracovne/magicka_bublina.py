import tkinter

velkost=100
farby=["red","blue","green","yellow","pink"]

def zmen_bublinu(udalost):
    platno.itemconfig(bublina,fill="white")
        
okno=tkinter.Tk()
okno.title("Bublina")    
platno=tkinter.Canvas(okno, height=300, width=300, bg="lightgray")
platno.pack()
bublina=platno.create_oval(150-velkost/2,150-velkost/2,150+velkost/2, 150+velkost/2,fill="red")
platno.bind_all("w",zmen_bublinu)
okno.mainloop()

