def obsah_obdlznika(a, b):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise ValueError('Nečíselná hodnota pre dĺžku strany obdĺžnika.')
    if a < 0 or b < 0:
        raise ValueError('Záporná hodnota pre dĺžku strany obdĺžnika.')
    return a * b


strana_a = input('a = ')
strana_b = input('b = ')
try:
    print(f'Obsah obdĺžnika je {obsah_obdlznika(strana_a, strana_b)}.')
except ValueError as chyba:
    print(chyba)
