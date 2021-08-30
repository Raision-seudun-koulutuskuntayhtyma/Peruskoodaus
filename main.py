# PÄÄOHJELMA

# Modulien ja kirjastojen lataukset
import hetutarkistus as ht


# Silmukka, jossa ollaan kunnes on syötetty järkevä henkilötunnus
hetu_jarkeva = False
while not hetu_jarkeva:
    # Kysytään käyttäjältä henkilötunnus
    kysytty_hetu = input('Anna henkilötunnus: ')

    # Tarkistetaan, että hetu on oikean pituinen
    pituus_oikein = ht.onko_pituus_oikein(kysytty_hetu)
    if pituus_oikein:

        # Tarkistetaan onko hetu oikein
        try:
            oli_oikein = ht.onko_hetu_oikeanlainen(kysytty_hetu)

            # Ilmoitetaan käyttäjälle oliko hetu oikein
            if oli_oikein:
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