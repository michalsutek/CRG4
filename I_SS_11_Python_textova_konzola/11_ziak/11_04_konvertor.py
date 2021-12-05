def prirad_kurz(kod):
    #kurzy k euru ku dnu 10. 1. 2018
    eur = 1         #1 EUR = 1 EUR          Slovensko
    czk = 25.57     #1 EUR = 25.57 CZK      Cesko
    huf = 309.92    #1 EUR = 309.92 HUF     Madarsko
    pln = 4.1814    #1 EUR = 4.1814 PLN     Polsko
    if kod == '1':
        return eur
    elif kod == '2':
        return czk
    elif kod == '3':
        return huf
    elif kod == '4':
        return pln
    else:
        return eur

def prepocet(z, do, suma):
    return do * suma / z


#vypis ponuky vstupnej meny
print('1 - euro (EUR)')
print('2 - česká koruna (CZK)')
print('3 - maďarský forint (HUF)')
print('4 - poľský zlotý (PLN)')

#nacitanie volby vstupnej meny - premenna mena_z
#TU DOPLNTE PROGRAMOVY KOD

#nacitanie vysky sumy na vymenu - premenna suma
#TU DOPLNTE PROGRAMOVY KOD

#vypis ponuky vystupnej meny
print('1 - euro (EUR)')
print('2 - česká koruna (CZK)')
print('3 - maďarský forint (HUF)')
print('4 - poľský zlotý (PLN)')

#nacitanie vystupnej meny – premenna mena_do)
#TU DOPLNTE PROGRAMOVY KOD

#priradenie kurzovej hodnoty vstupnej meny
kurz_z = prirad_kurz(mena_z)
#priradenie kurzovej hodnoty vystupnej meny
kurz_do = prirad_kurz(mena_do)
#vypis vysledku
print(f'{suma} => {prepocet(kurz_z, kurz_do, suma)}')
