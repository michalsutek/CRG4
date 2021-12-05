def plechovky_ks(sirka, dlzka, vydatnost):
    #vypocet plochy podlahy
    plocha_podlahy = sirka * dlzka
    pocet_plechoviek = plocha_podlahy // vydatnost
    if plocha_podlahy % vydatnost != 0:
        pocet_plechoviek = pocet_plechoviek + 1
    return pocet_plechoviek


#nacitanie vstupnych hodnot: rozmery podlahy, vydatnost plechovky
sirka = input('Šírka podlahy (v metroch): ')
dlzka = input('Dĺžka podlahy (v metroch): ')
vydatnost_farby = input('Výdatnosť plechovky farby (v m štvorcových): ')

#pretypovanie hodnot na ciselne (realne cisla)
sirka = float(sirka)
dlzka = float(dlzka)
vydatnost_farby = float(vydatnost_farby)

#vypisanie poctu plechoviek
print(f'Na premaľovanie podlahy potrebujeme {plechovky_ks(sirka, dlzka, vydatnost_farby)} ks plechoviek.')
