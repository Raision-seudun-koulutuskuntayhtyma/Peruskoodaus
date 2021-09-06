import stdnum.fi.hetu


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

if __name__ == '__main__':
    hetu = Henkilotunnus('010101-88XX')
    sukupuoli = hetu.sukupuoli()
    print("Henkilötunnuksen sukupuoli", sukupuoli)
