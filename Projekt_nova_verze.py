"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Petra Slámová
email: petja24@seznam.cz
"""
texts = ['''
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
users = {
    "bob" : "123",
    "ann": "pass123",
    "mike" : "password123",
    "liz" : "pass123"
} #uživatelé a hesla

name = input("Zadej své jméno: ")
password = input("Zadej heslo: ")
oddelovac = ("=" * 40) #oddělovač 
print(oddelovac + "\n" + oddelovac)

if users.get(name) == (password):
    print("Ahoj", name, "vítej v naší aplikaci!")
else:
    print("Neplatné jméno, nebo heslo. Program bude ukončen.")
    exit()

print(f"Vyber si jeden ze {len(texts)} textů k analyzování.")
print(oddelovac)
#uživatel nezadal číslo, ale jiný znak
vyber = input("Napiš číslo mezi 1 a 3. Vybral jsi: ")
if not vyber.isdigit(): 
    print("Nezadal jsi číslo. Program se ukončuje.")
    exit()
#uživatel zadal číslo mimo rozsah výběru
if vyber.isnumeric():
    vyber = int(vyber)  #převod výběru na číslo
    if vyber < 1 or vyber > 3:
        print("Nesprávná volba. Program se ukončuje.")
        exit()
print(oddelovac)
# Výběr textu
text = texts[vyber - 1]
pocet_slov = len(text.split())
slova_velke_pismeno = sum(1 for word in text.split() if word.istitle()) #počet slov psaných velkým písmenem na začátku
#počet slov psaných velkými písmeny
import string
slova_velkymi_pismeny = sum(1 for word in text.split() if word.isupper() and word.strip(string.punctuation).isalpha()) 
slova_mala_pismena = sum(1 for word in text.split() if word.islower()) #počet slov psaných malými písmeny
ciselne_retezce = sum(1 for word in text.split() if word.isdigit()) #počet číselných řetězců v textu
soucet_cisel = sum(int(word) for word in text.split() if word.isdigit()) #součet všech čísel
# výsledky všech operací výše
print(f"Ve vybraném textu je {pocet_slov} slov.")
print(f"Velkým písmenem začíná {slova_velke_pismeno} slov.")
print(f"Velkými písmeny je napsáno {slova_velkymi_pismeny} slov.")
print(f"Malými písmeny je napsáno {slova_mala_pismena} slov.")
print(f"V textu je celkem {ciselne_retezce} číselných řetězců.")
print(f"Součet všech čísel v textu je {soucet_cisel}.")

# poslední část je graf
print(oddelovac)
print(f" {'LEN':<3}|{'OCCURRENCES':^17}|{'NR.':>4}")
# seznamu délky každého slova
delka_slov = [len(word.strip(string.punctuation)) for word in text.split()]
# Vytvoření množiny délek slov
mnozina_delka = set(delka_slov)
# frekvence jednotlivých délek slov
frekvence_delka = []
for delka in mnozina_delka:
    frekvence_delka.append(delka_slov.count(delka))
nejvyssi_delka = max(frekvence_delka)
# tabulka
star = '*'
space = ' '
for delka in mnozina_delka:
    pocet_space = nejvyssi_delka - delka_slov.count(delka)
    print(f" {delka} | {star * delka_slov.count(delka)} {space * pocet_space} | {delka_slov.count(delka)}")
print(oddelovac)


