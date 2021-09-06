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
    syntynyt = syntymapaiva(hetu)
    tanaan = datetime.date.today()
    vuosiero = tanaan.year - syntynyt.year
    synttarit_tana_vuonna = syntynyt.replace(year=tanaan.year)
    if synttarit_tana_vuonna < tanaan:
        return vuosiero - 1
    return vuosiero