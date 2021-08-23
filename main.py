# HENKILÖTUNNUKSEN TARKISTUSSOVELLUS

# Kysytään käyttäjältä henkilötunnus - merkkijonono (string)
henkilotunnus = '130728-478N' #input('Anna henkilötunnus: ')

# Muutetaan henkilötunnus isoihin kirjaimiin
henkilotunnus = henkilotunnus.upper()

# Sanakirja vuosisatakoodin selvittämiseen
vuosisadat = {'+': 1800, '-': 1900, 'A': 2000}

# Sanakirja tarkisteiden hakemiseen
tarkisteet = {0: '0', 1: '1', 2: '2', 3: '3',
              4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'H', 17: 'J', 18: 'K', 19: 'L', 20: 'M', 21: 'N', 22: 'P', 23: 'R', 24: 'S', 25: 'T', 26: 'U', 27: 'V', 28: 'W', 29: 'X', 30: 'Y'}

# Erotetaan henkilötunnuksen osat omiin muuttujiinsa (merkkijonoja)
paivat_str = henkilotunnus[0] + henkilotunnus[1]
kuukaudet_str = henkilotunnus[2:4]
vuodet_str = henkilotunnus[4:6]
vuosisatakoodi_str = henkilotunnus[6]
jarjestysnumero_str = henkilotunnus[7:10]
tarkiste_str = henkilotunnus[10]

# Muutetaan merkkijonot numeroiksi
paivat = int(paivat_str)
kuukaudet = int(kuukaudet_str)
vuodet = int(vuodet_str)
vuosisata = vuosisadat[vuosisatakoodi_str]
syntymavuosi = vuosisata + vuodet

# Muutetaan syntymäajan päivämääräarvot tekstiksi -> syntympäivä
syntymaaika_str = str(paivat) + '.' + str(kuukaudet_str) + '.' + str(syntymavuosi)

print('Syntymäaika on', syntymaaika_str)
# print('Päivät:',paivat_str, 'kuukaudet', kuukaudet_str, 'vuodet', vuodet_str, 'vuosisatakoodi', vuosisatakoodi_str, 'järjestysnumero', jarjestysnumero_str)

# Tulostetaan syötetty henkilötunnus koneen ruudulle
# print('Antamasi henkilötunnus oli', henkilotunnus)
