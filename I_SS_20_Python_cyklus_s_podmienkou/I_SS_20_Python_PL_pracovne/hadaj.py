# Zjednodušená verzia hry Hádaj číslo
from random import *
cislo=randint(1,10)
print('Myslím si číslo od 1 do 10. Uhádni ho! :)')
pokus=1
while(pokus<=3):
    tip=int(input('Tvoj tip:'))
    if tip==cislo:
        print('Uhádol si!')
        break
    else:
        print('Neuhádol si!')
    pokus=pokus+1
print('KONIEC HRY')
