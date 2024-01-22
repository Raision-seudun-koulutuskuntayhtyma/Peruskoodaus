from eläimet import Kissa, Koira


def main():
    eläimet = luo_eläimet()

    # Tulosta eläimet
    print("Eläimet:")
    for eläin in eläimet:
        print(eläin)

    painot_yhteensä = sum(eläin.paino_kg for eläin in eläimet)
    print("Painot yhteensä:", painot_yhteensä)


def luo_eläimet():
    eläimet = []
    while True:  # Looppaa "ikuisesti"
        eläin = luo_eläin()
        if eläin is None:
            break  # Poistu loopista
        eläimet.append(eläin)
    return eläimet


def luo_eläin():
    nimi = input("Anna eläimen nimi (tai tyhjä jos haluat lopettaa): ")
    if not nimi:
        return None

    paino = None
    while paino is None:
        paino_teksti = input("Anna eläimen paino (kg): ")
        try:
            paino = float(paino_teksti.replace(",", "."))
        except Exception:
            print("Ei kelpaa. Painon pitää olla luku.")

    laji = None
    while laji is None:
        vastaus = input("Koira (O) vai kissa (I)? ")
        if vastaus.upper() == "O" or vastaus.lower() == "koira":
            laji = Koira
        elif vastaus.upper() == "I" or vastaus.lower() == "kissa":
            laji = Kissa
        else:
            print("Ei kelpa. Valitse O tai I.")

    eläin = laji(nimi, paino)
    return eläin


if __name__ == "__main__":
    main()
