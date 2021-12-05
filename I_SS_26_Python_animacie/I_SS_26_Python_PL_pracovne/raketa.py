import tkinter

okno=tkinter.Tk()
okno.title("Raketa")    
platno=tkinter.Canvas(okno, height=300, width=1000, bg="black")
platno.pack()
obrazok=tkinter.PhotoImage(file = 'raketa.gif')
raketa=platno.create_image(-75, 100, image = obrazok, anchor = "nw")
   
okno.mainloop()
