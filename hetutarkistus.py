# HENKILÖTUNNUKSEN TARKISTUSRUTIINI

def tarkista_hetu(hetu):
    """Tarkistaa, että henkilötunnus on oikein muodostettu
    käyttäen modulo 31 tarkistettta

    Args:
        hetu (string): Suomalainen henkilötunnus merkkijonona

    Returns:
        boolean: True, jos oikein, False, jos väärin
    """
    
    # Muutetaan henkilötunnus isoihin kirjaimiin
    hetu = hetu.upper()

    # Sanakirja vuosisatakoodin selvittämiseen
    vuosisadat = {'+': 1800, '-': 1900, 'A': 2000}

    # Sanakirja tarkisteiden hakemiseen
    tarkisteet = {0: '0', 1: '1', 2: '2', 3: '3',
                4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'H', 17: 'J', 18: 'K', 19: 'L', 20: 'M', 21: 'N', 22: 'P', 23: 'R', 24: 'S', 25: 'T', 26: 'U', 27: 'V', 28: 'W', 29: 'X', 30: 'Y'}

    # Erotetaan henkilötunnuksen osat omiin muuttujiinsa (merkkijonoja)
    paivat_str = hetu[0] + hetu[1]
    kuukaudet_str = hetu[2:4]
    vuodet_str = hetu[4:6]
    vuosisatakoodi_str = hetu[6]
    jarjestysnumero_str = hetu[7:10]
    tarkiste_str = hetu[10]

    # Yhdistetään merkkijonot luvuksi tarkisteen laskentaa varten 130 728 478
    luku_str = paivat_str + kuukaudet_str + vuodet_str + jarjestysnumero_str

    # Muutetaan numeroksi (int)
    luku = int(luku_str)

    # Lasketaan jakojäännös modulo 31
    jakojaannos = luku % 31

    # Haetaan jakojäännöstä vastaava kirjain tarkisteet-sanakirjasta
    uudelleen_laskettu_tarkiste = tarkisteet[jakojaannos]

    # Tarkistetaan onko laskettu tarkiste sama kuin syötetty tarkiste
    if uudelleen_laskettu_tarkiste == tarkiste_str:
        oikein = True
    else:
        oikein = False

    return oikein
