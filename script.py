"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Patrik Mareš
email: patamares@seznam.cz
discord: 
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

uzivatele={             #nacteni uzivatelskych jmen a hesla
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

uzivatelske_jmeno=input("Zadej uzivatelske jmeno: ")  #zadani uz. jmena
heslo=input("Zadej heslo: ")        #zadani hesla

if uzivatelske_jmeno in uzivatele and uzivatele.get(uzivatelske_jmeno) == heslo:        #overeni uzivatelskeho jmena a hesla, jestli je v databazi
    print("username: ",uzivatelske_jmeno, "\n"
          "password: ",heslo, "\n" ,
          "-" * 20, "\n"
          "Welcome to the app, ",uzivatelske_jmeno)

    print ("We have 3 texts to be analyzed.","\n",
           "-" * 20,
          )
else:   # kdyz uzivatel zada spatne udaje
   
    print("username: ",uzivatelske_jmeno, "\n"
          "password: ",heslo, "\n"
          "unregistered user, terminating the program..")
    
vyber=("1","2","3")     #moznosti vyberu textu

zvoleny_vyber = input("Enter a number btw. 1 and 3 to select: ")  #zvoleni textu, zadani cisla ktere musi byt 1-3
      
while zvoleny_vyber not in vyber:
    
    print("Nespravny vyber textu")     #pokud je zadane nespravne cislo
    break

print ("-" * 20)
          

text=TEXTS[int(zvoleny_vyber)-1]    #prebrani textu na cisla z vyberu

slova=text.split()                  #rozdeleni textu na slova
pocet_slov=len(slova)               #pocet slov

pocet_slov_zacinajici_velka_pismena = (0)       #pocitani slov, ktere zacinaji velkym pismenem, za kazde se pripise +1
for slovo in slova:
    if slovo.istitle():
        pocet_slov_zacinajici_velka_pismena+=1

pocet_slov_velka_pismena = (0)              #pocitani slov, ktere jsou cele z velkych pismen, za kazde se pripise +1
for slovo in slova:
    if slovo.isupper():
        pocet_slov_velka_pismena+=1

pocet_slov_mala_pismena = (0)           #pocitani slov, ktere jsou cele z malych pismen, za kazde se pripise +1
for slovo in slova:
    if slovo.islower():
        pocet_slov_mala_pismena+=1

pocet_cisel = (0)           #pocet cisel v textu
for slovo in slova:
    if slovo.isdigit():
        pocet_cisel+=1

soucet_cisel = (0)                       #soucet cisel v textu
for slovo in slova:
    if slovo.isdigit():
        soucet_cisel+=(int(slovo))
       
print(f"There are {pocet_slov} words in the selected text.")            #vypisou se pozadovane texty
print(f"There are {pocet_slov_zacinajici_velka_pismena} titlecase words.")
print(f"There are {pocet_slov_velka_pismena} uppercase words.")
print(f"There are {pocet_slov_mala_pismena} lowercase words.")
print(f"There are {pocet_cisel} numeric strings.")
print(f"The sum of all the numbers {soucet_cisel}.")

print ("-" * 20)







