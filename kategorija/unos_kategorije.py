from artikl import unos_artikla
from utilities import unos_cijelog_pozitivnog_broja
from .kategorija import Kategorija

def unos_kategorije(redni_broj):
    naziv = input(f"Unesite naziv {redni_broj}. kategorije: ")

    artikli = []
    br_artikala = unos_cijelog_pozitivnog_broja(f'Unesite broj artikala za {redni_broj}. kategoriju: ')
    for i in range(1, br_artikala + 1):
        artikli.append(unos_artikla(i))

    artikl = artikli

    return Kategorija(naziv, artikli)
