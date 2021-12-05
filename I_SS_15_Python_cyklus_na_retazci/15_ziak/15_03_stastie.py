def stastne_cislo(datum, cas):    #definujte funkciu s parametrami d (datum narodenia) a c (casovy usek dna)



datum = input('Zadajte dátum v tvare den.mesiac.rok: ') #nacitame datum narodenia pouzivatela
print('Ak ste sa narodili od 00:00 hod. vrátane do 06:00 hod., stlačte 1.') #vypiseme casove useky dna, ktore sledujeme
print('Ak ste sa narodili od 06:00 hod. vrátane do 13:00 hod., stlačte 2.')
print('Ak ste sa narodili od 13:00 hod. vrátane do 20:00 hod., stlačte 3.')
print('Ak ste sa narodili od 20:00 hod. vrátane do 24:00 hod., stlačte 4.')
cas = input('Vaša voľba: ') #nacitame kod zvoleneho casoveho useku dna

print(f'Vaše šťastné číslo: {stastne_cislo(datum, cas)}')   #vypiseme navratovu hodnotu funkcie stastne_cislo()
