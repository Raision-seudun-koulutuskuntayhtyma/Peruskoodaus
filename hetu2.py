import datetime

VUOSISADAT = {
    '+': 1800,
    '-': 1900,
    'A': 2000,
}

def sukupuoli(hetu):
    toiseksi_viimenen_merkki = hetu[-2]
    luku = int(toiseksi_viimenen_merkki)
    if luku % 2 == 0:  # jakojäännös 2:lla == 0
        return "Nainen"  # parillinen = 0, 2, 4, 6, 8
    else:
        return "Mies"  # pariton = 1, 3, 5, 7, 9

def syntymapaiva(hetu):
    paivays = datetime.datetime.strptime(hetu[:6], "%d%m%y").date()
    vuosisata = VUOSISADAT[hetu[6]]  # välimerkki -> vuosisata
    return paivays.replace(year=(vuosisata + (paivays.year % 100)))


def ika(hetu):
    paivays = syntymapaiva(hetu)
    # FIXME: Laske ikä oikein
    aikaero = datetime.date.today() - paivays
    return int(aikaero.total_seconds() / 3600 / 24 / 365)
