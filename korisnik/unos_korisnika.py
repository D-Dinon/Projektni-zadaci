from utilities import unos_cijelog_pozitivnog_broja
#from utilities import unos_godina
from .korisnik import Korisnik

def unos_korisnika(redni_broj):
    ime= input(f'Unesite ime {redni_broj}. korisnika: ').capitalize()
    prezime = input(f'Unesite prezime {redni_broj}. korisnika: ').capitalize()
    telefon = unos_cijelog_pozitivnog_broja(f'Unesite telefon {redni_broj}. korisnika: ')
    email = input(f'Unesite email {redni_broj}. korisnika: ').strip()
    #godine = unos_godina(f'Unesite godine {redni_broj}. korisnika')
    return Korisnik(ime, prezime, email, telefon)
