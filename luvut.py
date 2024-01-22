"""
Lukuihin liittyviä toimintoja.
"""

def vertaa_lukuja(luku1, luku2):
    """
    Vertaa kahden luvun suuruutta.
    """
    if luku1 > luku2:
        print("Luku on suurempi kuin", luku2)
    elif luku1 == luku2:
        print("Luku on tarkalleen", luku2)
    else:
        print("Luku on pienempi kuin", luku2)
