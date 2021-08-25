# PÄÄOHJELMA

# Modulien ja kirjastojen lataukset
import hetutarkistus as ht

# Kysytään käyttäjältä henkilötunnus
kysytty_hetu = input('Anna henkilötunnus: ')

# Tarkistetaan onko hetu oikein
oli_oikein = ht.tarkista_hetu(kysytty_hetu)

# Ilmoitetaan käyttäjälle oliko hetu oikein
if oli_oikein == True:
    print('Henkilötunnus OK')
else:
    print('Henkilötunnus väärin, tarkista!')
