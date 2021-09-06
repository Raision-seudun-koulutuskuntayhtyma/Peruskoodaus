import hetu3

class VakioHetu:
    def __str__(self):
        return "HETU42"

    def ika(self):
        return 42


def main():
    ht = hetu3.Henkilotunnus('260283-242L')
    ht2 = VakioHetu()
    nayta_ika(ht)
    nayta_ika(ht2)


def nayta_ika(h):
    print(f"Henkilötunnuksen {h} ikä on {h.ika()}")


if __name__ == '__main__':
    main()
