DANAŠNJI_DATUM = '5.5.2017'


class Stranka:
    def _init_(self, ime, priimek, datum_rojstva):
        self.ime = ime
        self.priimek = priimek
        self.datum_rojstva = datum_rojstva

    def Nastavi_starost(self,datum_rojstva=self.datum_rojstva, današnji_datum=DANAŠNJI_DATUM):
        #zračuni starost
        #preveri če čez 18 - če ni error
        self.starost =

    def _repr_(self):
        return 'Stranka({}, {}, {})'.format(self.ime, self.priimek, self.datum_rojstva)

    def _str_(self):
        return '{} {}, datum rojstva: {}'.format(self.ime, self.priimek, self.datum_rojstva)


class Nezgodno_zavarovanje:
    def _init_(self, trajanje):
        self.trajanje = trajanje
        
    def Nastavi_lastnika(self, stranka):
        self.lastnik = stranka

    def Nastavi_premijo(self, interval_plačevanja, trajanje = self.trajanje, starost=self.lastnik.starost):
        #zračuni premijo glede na starost in interval plačevanja
        #pokaži kok bi mogl plačvat

    def Ustvari_zavarovanje(self):
        #ustvari oz dodaj v datoteko zavarovanje
        #dodaj lastnika v bazo oseb (če še ni)

        
    def _str_(self):
        return 'Nezgodno zavarovanje št. {}, lastnik: {}'.format(self.številka, self.lastnik)

    def _repr_(self):
        return 'Nezgodno_zavarovanje({})'.format(self.trajanje)
