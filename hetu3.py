import datetime

import stdnum.fi.hetu

VUOSISADAT = {
    '+': 1800,
    '-': 1900,
    'A': 2000,
}


class Henkilotunnus:
    def __init__(self, teksti):
        if not stdnum.fi.hetu.is_valid(teksti):
            raise Exception(f"Ei ole kelvollinen hetu: {teksti}")
        self.hetu = teksti  # aseta attribuuttiin "hetu" muuttujan teksti sisältö

    def sukupuoli(self):
        toiseksi_viimenen_merkki = self.hetu[-2]
        luku = int(toiseksi_viimenen_merkki)
        if luku % 2 == 0:  # jakojäännös 2:lla == 0
            return "Nainen"  # parillinen = 0, 2, 4, 6, 8
        else:
            return "Mies"  # pariton = 1, 3, 5, 7, 9

    def syntymapaiva(self):
        paivays = datetime.datetime.strptime(self.hetu[:6], "%d%m%y").date()
        vuosisata = VUOSISADAT[self.hetu[6]]  # välimerkki -> vuosisata
        return paivays.replace(year=(vuosisata + (paivays.year % 100)))

    def ika(self):
        syntynyt = self.syntymapaiva()
        tanaan = datetime.date.today()
        vuosiero = tanaan.year - syntynyt.year
        synttarit_tana_vuonna = syntynyt.replace(year=tanaan.year)
        viettanyt_jo = (synttarit_tana_vuonna <= tanaan)
        return (vuosiero if viettanyt_jo else vuosiero - 1)


if __name__ == '__main__':
    hetu_objekti = Henkilotunnus('010101-888B')
    sukupuoli = hetu_objekti.sukupuoli()
    print("Henkilötunnuksen sukupuoli", sukupuoli)
    ika = hetu_objekti.ika()
    print("Ikä:", ika)
