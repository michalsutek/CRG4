povodny_text="""From: Jason Faulkner <p.polak@inymail.sk>
To: “jarko23@gmail.com” <jarko23@gmail.com>
Date: Tue, 8 Jan 2019 11:30:48 -0500
Subject: Ukazkovy mail"""
upraveny_text=povodny_text.split()    # upraví pôvodný dlhý text na zoznam jednotlivých slov, ktoré boli oddelené medzerami
print(upraveny_text)
emailove_adresy=[]
# tu doplňte program na vyfiltrovanie e-mailových adries
# ...
# tu pokračuje program
if emailove_adresy==[]:
    print("\nNeboli nájdené žiadne e-mailové adresy!")
else:
    print("\nNájdené e-mailové adresy:")
    for adresa in emailove_adresy:
        print(adresa)
    
