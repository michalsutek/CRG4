import tkinter

okno=tkinter.Tk()
okno.title("Semafor")    
platno=tkinter.Canvas(okno, height=300, width=300, bg="white")
platno.pack()
platno.create_rectangle(50,0,250,300,fill="black")
cervena=platno.create_oval(100,0,200,100,fill="white")
zlta=platno.create_oval(100,100,200,200,fill="white")
zelena=platno.create_oval(100,200,200,300,fill="white")
okno.mainloop()
