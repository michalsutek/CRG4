meno = input('Zadajte svoje meno: ')    #cez konzolu zadavajte rozne vstupne retazce a sledujte vypis programu v konzole
if meno.isalpha() and meno[0] == meno[0].upper():
    print(f'Zadané meno {meno} je v poriadku.')
else:
    print(f'Zadané meno {meno} nie je v poriadku.')





