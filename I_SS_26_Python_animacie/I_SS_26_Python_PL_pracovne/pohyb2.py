import tkinter

velkost=20

def pohybuj_loptickou():
    for i in range(10):
        x=i
        y=x
        platno.coords(lopticka,x,y,x+velkost,y+velkost)
        platno.update()
        platno.after(100)
        
okno=tkinter.Tk()
okno.title("Pohyb")    
platno=tkinter.Canvas(okno, height=400, width=400, bg="lightgray")
platno.pack()
lopticka=platno.create_oval(0,0,velkost,velkost,fill="red")
pohybuj_loptickou()
okno.mainloop()

