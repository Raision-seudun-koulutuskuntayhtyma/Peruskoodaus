# PÄÄOHJELMA

# Modulien ja kirjastojen lataukset
import hetutarkistus as ht

# Silmukka, jossa ollaan kunnes on syötetty järkevä henkilötunnus
hetu_jarkeva = False
while hetu_jarkeva == False:
    # Kysytään käyttäjältä henkilötunnus
    kysytty_hetu = input('Anna henkilötunnus: ')

    # Tarkistetaan, että hetu on oikean pituinen
    pituus_oikein = ht.tarkista_pituus(kysytty_hetu)
    if pituus_oikein == True:

        # Tarkistetaan onko hetu oikein
        try:
            oli_oikein = ht.tarkista_hetu(kysytty_hetu)

            # Ilmoitetaan käyttäjälle oliko hetu oikein
            if oli_oikein == True:
                print('Henkilötunnus OK')
                print('Sukupuoli:', ht.selvita_sukupuoli(kysytty_hetu))
                print('Hän on syntynyt', ht.syntymapaiva(kysytty_hetu))
                hetu_jarkeva = True
                # TODO: lisää tähän ikäfunktio
            else:
                print('Henkilötunnus väärin, tarkista!')
                hetu_jarkeva = False
        except:
            print('Henkilötunnuksessa virheellinen merkki, syötä uudelleen!')
            hetu_jarkeva = False
    else:
        print('Henkilötunnuksen pituus väärä, syötä uudelleen!')
        hetu_jarkeva = False