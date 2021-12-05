def hodnota_na_konci_mesiaca(mesiac):
    try:
        #overujeme celociselnost
        mesiac = int(mesiac)
    except ValueError:
        raise ValueError('Počet mesiacov nie je číslo.')
    if mesiac <= 0:
        raise ValueError('Počet mesiacov nie je prirodzené číslo.')
    hodnota = mesiac * 2
    return hodnota


#pocet mesiacov investovania
pocet_mesiacov = input('Počet mesiacov: ')
print(f'na konci {pocet_mesiacov}. mesiaca: {hodnota_na_konci_mesiaca(pocet_mesiacov):5}')

