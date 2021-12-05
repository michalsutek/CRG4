import tkinter
okno=tkinter.Tk()
okno.title("Hviezdna obloha")

def obloha():
    platno.delete("all")    #vymaže všetky predtým nakreslené objekty na plátne
    # tu doplňte kód na vykreslenie hviezd
    # ...    
    platno.update()         #zobrazí všetky nakreslení objekty na plátne
    
platno=tkinter.Canvas(okno, height=300, width=300, bg="black")
platno.pack()
tkinter.Button(okno,text="Generuj oblohu",command=obloha).pack()
okno.mainloop()

