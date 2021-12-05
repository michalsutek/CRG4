def obsah_obdlznika(a, b):
    return a * b


strana_a = input('a = ')
strana_b = input('b = ')
try:
    strana_a = float(strana_a)
    strana_b = float(strana_b)
except ValueError:
    print('Nečíselná hodnota pre dĺžku strany obdĺžnika.')
else:
    print(f'Obsah obdĺžnika je {obsah_obdlznika(strana_a, strana_b)}.')
