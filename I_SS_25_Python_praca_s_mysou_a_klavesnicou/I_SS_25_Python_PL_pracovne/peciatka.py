import tkinter

velkost=20

def opeciatkuj_cervenou(udalost):
    x=udalost.x
    y=udalost.y
    platno.create_oval(x-velkost/2,y-velkost/2,x+velkost/2, y+velkost/2,fill="red")
        
okno=tkinter.Tk()
okno.title("Bublina")    
platno=tkinter.Canvas(okno, height=300, width=300, bg="lightgray")
platno.pack()
platno.bind("<Button-1>",opeciatkuj_cervenou)
okno.mainloop()

