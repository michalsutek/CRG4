vyska = float(input("Zadaj vysku v metroch \n")) # nacitanie vysky a vahy, float prevedie udaje na desatinne cisla
vaha = float(input("Zadaj vahu v kilogramoch \n"))

bmi = vaha/(vyska**2) # vypocet BMI
print("Tvoj BMI = ", bmi) # vypis bmi

if bmi < 19:    # zistujeme ci ma subjekt nadvahu, normalnu vahu alebo podvahu a vysledok vypiseme na obrazovku
    print("Mas podvahu")
elif bmi < 25:
    print("Mas normalnu vahu")
elif bmi < 31:
    print("Mas nadvahu")
else:
    print("Mas obezitu")

