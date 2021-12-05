import turtle
def kresli_riadok(riadok, d):                 # vykresli jeden riadok vzoru
    for znak in riadok:                       # prechadzame znaky riadku
        if znak == 'x':                       # ak je znak x, vykreslime cervenu bodku
            p.dot(d, 'red')
        elif znak == 'o':                     # ak je znak o, vykreslime modru bodku
            p.dot(d, 'blue')
        p.forward(d)                          # posunieme pero na poziciu dalsej bodky
    p.backward(len(riadok) * d)               # po ukonceni cyklu/vykresleni riadku presunieme pero na zaciatok tohto riadku

def kresli_vzor(vzor, d):
    pocet_riadkov = vzor.count('/')         # pocet riadkov vzoru
    for riadok in range(pocet_riadkov):     # postupne spracujeme/vykreslime jednotlive riadky
        koniec_riadku = vzor.find('/')           # pocet riadkov je urceny poctom znakov / v retazci vzor
        vzor_riadok = vzor[:koniec_riadku]       # pomocou vyrezu vyberieme prvy riadok vzoru
        kresli_riadok(vzor_riadok, priemer) # vykreslime vybrany riadok
        vzor = vzor[koniec_riadku + 1:]          # zo vzoru odstranime riadok, ktory sme prave vykreslili
        # presun pera do noveho riadku (pero skoncilo na zaciatku uz vykresleneho riadku)
        p.right(90)
        p.forward(d)
        p.left(90)


p = turtle.Turtle()
t = turtle.Screen()
p.penup()
p.speed(0)
# velkost - priemer bodu reprezentujuceho koralik
priemer = 20

# zasobnik vzorov na experimentovanie
#vzor = 'nnnx/nnxx/nxxx/xxxx/oxxo/'
#vzor = 'nnnnx/nnnxx/nnxxx/nxxsx/xoxxo/xoxxo/nxxxx/nnxxx/nnnxx/nnnnx/'
#vzor = 'nxxx/oxxx/nnox/'
#vzor = 'xx///xx/'
vzor = 'xxo/nxo/'

kresli_vzor(vzor, priemer)
#vzor = zrkadlo(vzor)       # riesenie ulohy 6
#kresli_vzor(vzor, priemer) # riesenie ulohy 6

p.hideturtle()
t.mainloop()
