class Vozilo:

    def __izracunaj_kw(self, snaga):  #privatna
        return int(snaga*0.735)

    def cijena_osiguranja(self, snaga):  #javna metoda
        kilovati = self.__izracunaj_kw(snaga)
        return kilovati*15
