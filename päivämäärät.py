from datetime import date, datetime, time

vuoden_eka_pvm = date(2024, 1, 1)

tänään = date.today()

print("Joku päivä:", vuoden_eka_pvm.strftime("%d.%m.%Y"))

print("Tänään on", tänään)

teksti = f"Tänään on {tänään:%d.%m.%Y}. Joku toinen päivä on {vuoden_eka_pvm}."

print(teksti)

erotus = tänään - vuoden_eka_pvm  # päivämäärien erotus on timedelta-tyyppinen

print(f"On kulunut melkein {erotus.days + 1} päivää vuoden alusta.")

nyt = datetime.now()

# HUOM!
# %S = ajan sekunnit, mutta
# %s = UNIX-aika, eli kuinka monta sekuntia on kulunut 1.1.1970 klo 00:00 jälkeen
# %M = ajan minuutit, mutta
# %m = kuukausi (kahdella numerolla)
# %Y = vuosi neljällä numerolla
# %y = vuosi kahdella numerolla

print(f"Nyt on {nyt:%d.%m.%y} klo {nyt:%H:%M:%S}")


vuoden_alku = datetime(2024, 1, 1, 0, 0, 0)

# Kahden datetime-tyypin erotus on timedelta-tyyppinen
va = nyt - vuoden_alku

# timedelta:lla on total_seconds-metodi, jolla saadaan muutettua
# kahden aikaleiman erotus sekunneiksi
print(f"Vuoden alusta on kulunut {va.total_seconds():.0f} sekuntia")

print(f"Vuoden alusta on kulunut {va.days} päivää ja {va.seconds} sekuntia.")

# Muutetaan sekunnit tunneiksi, minuuteiksi ja sekunneiksi:
va_aika = time(
    hour=va.seconds // 60 // 60,  # tunnit -> jaetaan 60:llä kahteen kertaan
    minute=(va.seconds // 60) % 60,  # minuutit -> jaetaan 60:llä ja jakojäännös 60:llä
    second=va.seconds % 60,  # sekunnit -> jakojäännös 60:llä
)

print(
    f"Vuoden alusta on kulunut {va.days} päivää, "
    f"{va_aika.hour} tuntia, {va_aika.minute} minuuttia "
    f"ja {va_aika.second} sekuntia."
)

