def desifruj(s):
    if len(s) % 2 == 0:
        vysledok = s[::2]
    else:
        raise ValueError('Chyba šifrovania')
    return vysledok


odkaz = input('Zadaj zašifrovaný odkaz: ')
try:
    print(f'Odkaz: {desifruj(odkaz)}')
except ValueError as chyba:
    print(chyba)
