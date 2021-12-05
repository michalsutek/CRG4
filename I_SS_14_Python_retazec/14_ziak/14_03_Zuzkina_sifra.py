def desifruj(s):
    if len(s) % 2 == 0:
        vysledok = ''
        for i in range(0, len(s), 2):
            vysledok = vysledok + s[i]
    else:
        raise ValueError('Chyba šifrovania')
    return vysledok


odkaz = input('Zadaj zašifrovaný odkaz: ')
try:
    print(f'Odkaz: {desifruj(odkaz)}')
except ValueError as chyba:
    print(chyba)

