import math
g = 9.81 #priblizna hodnota gravitacneho zrychlenia
dlzka = input('Dĺžka lana: ')
dlzka = float(dlzka)
cas_padu = math.sqrt(2 * dlzka / g)
print(f'Voľný pád bude trvať {cas_padu} s.')
