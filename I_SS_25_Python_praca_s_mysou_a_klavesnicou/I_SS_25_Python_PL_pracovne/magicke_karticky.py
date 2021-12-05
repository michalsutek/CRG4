import tkinter

velkost=50
        
okno=tkinter.Tk()
okno.title("Magické kartičky")    
platno=tkinter.Canvas(okno, height=200, width=400, bg="lightgray")
platno.pack()
platno.create_text(200,25,text="Klikni na kartičku, aby si zmenil jej farbu!")
karta_1=platno.create_rectangle(100-velkost/2,100-velkost,100+velkost/2, 100+velkost,fill="white")
karta_2=platno.create_rectangle(200-velkost/2,100-velkost,200+velkost/2, 100+velkost,fill="white")
karta_3=platno.create_rectangle(300-velkost/2,100-velkost,300+velkost/2, 100+velkost,fill="white")
okno.mainloop()

