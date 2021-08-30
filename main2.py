import stdnum.fi.hetu

import hetu2

def main():
    while True:
        hetu = input("Anna HETU: ")
        if stdnum.fi.hetu.is_valid(hetu):
            print("Oikeanlainen HETU")
            print(hetu2.sukupuoli(hetu))
            print("Syntymäpäivä:", hetu2.syntymapaiva(hetu))
            print("Ikä:", hetu2.ika(hetu))
            break
        else:
            print("Vääränlainen HETU")


if __name__ == '__main__':
    main()
