original=["1111", "0110", "0000", "1111"]
volba=input("Chceš vykresliť originál (O) alebo negatív (N)?")
if volba=="O" or volba=="o":
    for riadok in original:
        print(riadok)
elif volba=="N" or volba=="n":
    negativ=[]
    # tu doplňte chýbajúci program pre vytvorenie negatívu
    # ...
    # tu pokračuje pôvodný program
    for riadok in negativ:
        print(riadok)
else:
    print("Zadal si nesprávnu voľbu!")
    
