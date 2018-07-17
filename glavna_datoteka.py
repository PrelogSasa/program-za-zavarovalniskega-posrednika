DANAŠNJI_DATUM = '5.5.2017'


class Stranka:
    def _init_(self, ime, priimek, datum_rojstva):
        self.ime = ime
        self.priimek = priimek
        self.datum_rojstva = datum_rojstva

    #def Nastavi_starost(self,datum_rojstva=self.datum_rojstva, današnji_datum=DANAŠNJI_DATUM):
        #zračuni starost
        #preveri če čez 18 - če ni error
        #self.starost =

    def _repr_(self):
        return 'Stranka({}, {}, {})'.format(self.ime, self.priimek, self.datum_rojstva)

    def _str_(self):
        return '{} {}, datum rojstva: {}'.format(self.ime, self.priimek, self.datum_rojstva)


class Nezgodno_zavarovanje:
    def _init_(self, trajanje, paket):
        self.trajanje = trajanje
        self.paket = paket
        with open('številka_zavarovanja.txt') as dat:
            številka_zavarovanja = dat.readline()
        self.številka = številka_zavarovanja
        with open('številka_zavarovanja.txt', 'w') as dat:
            številka_zavarovanja_večja = int(self.številka) + 1
            številka_zavarovanja_string = str(številka_zavarovanja_večja).zfill(6)
            dat.write(številka_zavarovanja_string)
            

    def _str_(self):
        return 'Nezgodno zavarovanje št. {}, lastnik: {}'.format(self.številka, self.lastnik)

    def _repr_(self):
        return 'Nezgodno_zavarovanje({}, {})'.format(self.trajanje, self.paket)
        
    def Nastavi_lastnika(self, stranka):
        self.lastnik = stranka 

    def Nastavi_premijo(self, interval_plačevanja, trajanje=self.trajanje, starost=self.lastnik.starost, paket=self.paket):
        trajanje = {1: 1, 5: 0.95, 10: 0.85}
        paketi = {'velik': 200, 'majhen': 150}
        if starost >= 65:
            k = 1.2
        else:
            k = 1
        premija = trajanje.get(trajanje) * k * paketi.get(paket) * trajanje
        self.premija = premija
        if interval_plačevanja == 'mesečno':
            plačilo = premija / trajanje / 12
            return 'Vaše mesečno plačilo je {}'.format(plačilo)
        else:
            plačilo = premija / trajanje
            return 'Vaše letno plačilo je {}'.format(plačilo)

    #def Ustvari_zavarovanje(self):
        #ustvari oz dodaj v datoteko zavarovanje
        #dodaj lastnika v bazo oseb (če še ni)

        
    

#def dodaj_stranko_na_seznam(stranka):
    
    
