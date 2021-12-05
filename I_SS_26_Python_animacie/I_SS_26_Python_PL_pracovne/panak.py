import tkinter

okno=tkinter.Tk()
okno.title("Panák")    
platno=tkinter.Canvas(okno, height=400, width=400, bg="white")
platno.pack()
platno.create_oval(150,50,250,150,fill="white")
platno.create_line(150,150,250,150)
platno.create_line(200,150,200,300)
platno.create_line(150,300,250,300)
l_ruka=platno.create_line(150,150,150,250)
p_ruka=platno.create_line(250,150,250,250)
l_noha=platno.create_line(150,300,150,400)
p_noha=platno.create_line(250,300,250,400)
   
okno.mainloop()
