objem_kecupu = input('Objem kečupu (v litroch): ')
objem_flase = input('Objem fľaše (v litroch): ')
try:
    objem_kecupu = float(objem_kecupu)
    objem_flase = float(objem_flase)
    pocet_flias = objem_kecupu // objem_flase
except ValueError:
    print('Na vstupe nebol číselný údaj.')
except ZeroDivisionError:
    print('Objem fľaše nemôže byť nulový.')
else:
    print(f'Počet fliaš: {pocet_flias}')
