class Eläin:
    def __init__(self, nimi, paino_kg):
        self.nimi = nimi
        self.paino_kg = paino_kg

    def tervehdi(self):
        print("Moi! Olen", self.nimi)

    def nuku(self):
        print("Zzzz..")

    def __str__(self):
        return type(self).__name__ + ": " + self.nimi

    # def __repr__(self):  # repr = representation eli esitys
    #     return "<" + type(self).__name__ + ": " + self.nimi + ">"

class Koira(Eläin):
    def tervehdi(self):
        print("Hau! Hau!")


class Kissa(Eläin):
    def tervehdi(self):
        print("Miau!")

    def nuku(self):
        print("Purr...")


if __name__ == "__main__":
    # Luodaan kaksi oliota (object), koira ja kissa:
    koira = Koira("Musti", 12)
    kissa = Kissa("Kisu", 4)

    # lista-muuttuja alla on list-luokan olio
    lista = [1, 2, 3]

    # Attribuuttien käyttäminen onnistuu pisteen avulla
    print("Koiran nimi:", koira.nimi)
    print("Kissan nimi:", kissa.nimi)
    print("Koiran paino:", koira.paino_kg, "kg")
    print("Kissan paino:", kissa.paino_kg, "kg")

    print("Kutsutaan tervehdi-metodia koirasta ja kissasta:")
    koira.tervehdi()
    kissa.tervehdi()

    print("Kokeillaan nuku-metodia:")
    koira.nuku()
    kissa.nuku()
