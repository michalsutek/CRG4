suma = input('Zadaj sumu, ktorú chceš investovať do kúpy poukazov: ')
suma = float(suma)
#doplnte vypocet poctu jednotlivych typov poukazov


#vypis poctu jednotlivych poukazov
print('Počty zakúpených darčekových poukazov;')
vypis = ' ks darčekových poukazov v hodnote '
print(f'Kúpte {pocet20} {vypis} 20 EUR.')
print(f'Kúpte {pocet10} {vypis} 10 EUR.')
print(f'Kúpte {pocet05} {vypis} 5 EUR.')
print(f'Kúpte {pocet01} {vypis} 1 EUR.')
print(f'Výdavok: {suma % 1}')
