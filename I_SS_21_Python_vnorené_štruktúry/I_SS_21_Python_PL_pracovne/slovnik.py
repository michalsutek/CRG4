import random

anglicky=['dog','cat','mouse','house']
slovensky=['pes','mačka','myš','dom']
pocet_slov=len(anglicky)
pocet_spravnych=0
for i in range(pocet_slov):
    print(anglicky[i])
print(f'Celkový počet správnych je {pocet_spravnych} z {pocet_slov}.')
    
