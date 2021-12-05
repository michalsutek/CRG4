import tkinter 

def napis_vysledok():
    if int(vstup.get())>0:
        vysledok.set("Je to kladné číslo")
    elif int(vstup.get())==0:
        vysledok.set("Je to nula")
    else:
        vysledok.set("Je to záporné číslo")

def koniec():
    okno.destroy()
    
okno=tkinter.Tk()
okno.title("Test čísla")
tkinter.Label(okno, text="Zadaj číslo:", bg="white",width=30).pack()
vstup = tkinter.StringVar()
tkinter.Entry(okno, textvariable=vstup).pack()
tkinter.Label(okno, text="Výsledok:", bg="white",width=30).pack()
vysledok=tkinter.StringVar()
tkinter.Entry(okno, textvariable=vysledok).pack()

tkinter.Button(okno,width=30, text="otestuj", command=napis_vysledok).pack()
tkinter.Button(okno,width=30, text="zruš", command=koniec).pack()

okno.mainloop()
