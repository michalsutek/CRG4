#funkcia na prevod teploty
def prevod(jednotka, teplota):
    if jednotka == 'C':
        return 9 * teplota / 5 + 32
    else:
        return 5 * (teplota - 32 )/ 9


#hlavny program
retazec = input('Zadajte hodnotu teploty spolu s jednotkou teploty (oddelené práve jednou medzerou): ')



