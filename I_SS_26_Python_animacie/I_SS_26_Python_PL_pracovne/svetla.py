import tkinter
import random
kody=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

okno=tkinter.Tk()
okno.title("Svetlá")    
platno=tkinter.Canvas(okno, height=300, width=300, bg="gray")
platno.pack()
prva=platno.create_oval(10,180,50,280,fill="white")
druha=platno.create_oval(70,180,110,280,fill="white")
tretia=platno.create_oval(130,180,170,280,fill="white")
stvrta=platno.create_oval(190,180,230,280,fill="white")
piata=platno.create_oval(250,180,290,280,fill="white")
for i in range(5):
    platno.create_rectangle(20+i*60,300,40+i*60,270,fill="black")
   
okno.mainloop()
