"""
Ensimmäinen Python-harjoitus.

Kokeillaan Python-ohjelmoinnin perusasioita.
"""

import nimet
from luvut import vertaa_lukuja

print("MUUTTUJAT JA FUNKTIOKUTSUT=========================================")

luku = 123          # kokonaisluku / integer (int)
etunimi = "Tuomas"  # merkkijono / string (str)
liukuluku = 2.5     # liukuluku / floating point number (float)

print("luku", luku)

print("Tulostetaan etunimi funktion avulla:")
nimet.tulosta_nimi(etunimi)

print("Liukuluku on:", liukuluku)
print("Verrataan liukulukua vertaa_lukuja-funktiolla")
vertaa_lukuja(liukuluku, 1)
vertaa_lukuja(liukuluku, 2)
vertaa_lukuja(liukuluku, 3)
vertaa_lukuja(liukuluku, 2.5)


print("LISTA ============================================================")

lista = [         # lista / list (list)
    "listan eka itemi",
    "listan toka itemi",
    123,
    44.4,
    3888,
]

print("Tulostetaan lista:")
for alkio in lista:
    print(alkio)


print("SANAKIRJA =========================================================")

juttuja = {         # sanakirja / dictionary (dict)
    "eka": 100,
    "toka": 200,
    "kolmas": 300,
}

print("Sanakirjan voi tulostaa ihan sellaisenaan:")
print(juttuja)

print("Sanakirjan avaimet voidaan käydä läpi for-loopilla:")
for avain in juttuja:
    print(avain)

print("Arvot saadaan, kun kutsutaan values-metodia:")
for arvo in juttuja.values():
    print(arvo)

print("Avaimet ja arvot saadaan pareina käyttäen items-metodia:")
for avain, arvo in juttuja.items():
    print(avain, arvo)

print("--- Sanakirjasta hakeminen:")

print("Avainta 'eka' vastaava arvo:")
print(juttuja["eka"])
print("toka:")
print(juttuja["toka"])
print("kolmas:")
print(juttuja.get("kolmas"))
print("neljäs:")
print(juttuja.get("neljäs"))

print("Sanakirjaan uuden arvon lisääminen:")
juttuja["neljäs"] = 400

print("nyt neljäs on:")
print(juttuja["neljäs"])

print("tai")
print(juttuja.get("neljäs"))
