DANAŠNJI_DATUM = '5.5.2017'


class Stranka:
    def __init__(self, ime, priimek, starost):
        self.ime = ime
        self.priimek = priimek
        self.starost = starost

    def __repr__(self):
        return 'Stranka({}, {}, {})'.format(self.ime, self.priimek, self.starost)

    def __str__(self):
        return '{} {}, starost: {}'.format(self.ime, self.priimek, self.starost)


class Nezgodno_zavarovanje:
    def __init__(self, trajanje, paket):
        self.trajanje = trajanje
        self.paket = paket
        with open('številka_zavarovanja.txt') as dat:
            številka_zavarovanja = dat.readline()
        self.številka = številka_zavarovanja
        with open('številka_zavarovanja.txt', 'w') as dat:
            številka_zavarovanja_večja = int(self.številka) + 1
            številka_zavarovanja_string = str(številka_zavarovanja_večja).zfill(6)
            dat.write(številka_zavarovanja_string)
            

    def __str__(self):
        return 'Nezgodno zavarovanje št. {}, lastnik: {}'.format(self.številka, self.lastnik)

    def __repr__(self):
        return 'Nezgodno_zavarovanje({}, {})'.format(self.trajanje, self.paket)
        
    def nastavi_lastnika(self, stranka):
        self.lastnik = stranka
    
    def nastavi_premijo(self, interval_plačevanja):
        if self.lastnik.starost >= 65:
            k = 1.2
        else:
            k = 1
        trajanja = {1: 1, 5: 0.95, 10: 0.85}
        paketi = {'velik': 200, 'majhen': 150}
        self.premija = trajanja.get(self.trajanje) * k * paketi.get(self.paket) * self.trajanje
        if interval_plačevanja == 'mesečno':
            plačilo = self.premija / self.trajanje / 12
            return 'Vaše mesečno plačilo je {}'.format(plačilo)
        else:
            plačilo = self.premija / self.trajanje
            return 'Vaše letno plačilo je {}'.format(plačilo)

    def ustvari_zavarovanje(self):
        #ustvari oz dodaj v datoteko zavarovanje
        with open('baza_oseb.txt', 'a') as baza_oseb:
            pass
        with open('baza_oseb.txt') as baza_oseb:
            osebe = baza_oseb.readlines()
        lastnika_ni_v_bazi = True
        for i in range(len(osebe)):
            if osebe[i].startswith('{}, {}, {}'.format(self.lastnik.ime, self.lastnik.priimek, self.lastnik.starost)):
                osebe[i] = osebe[i].strip() + ', {}\n'.format(self.številka)
                lastnika_ni_v_bazi = False
                break
        if lastnika_ni_v_bazi:
            osebe += ['{}, {}, {}: {}'.format(self.lastnik.ime, self.lastnik.priimek, self.lastnik.starost, self.številka)]
        with open('baza_oseb.txt', 'w') as baza_oseb:
            for vrstica in osebe:
                baza_oseb.write(vrstica)

        
##Domen = Stranka('Maja', 'Kos', 19)
##Zavarovanje2= Nezgodno_zavarovanje(10, 'velik')
##Zavarovanje2.nastavi_lastnika(Domen)
##Zavarovanje2.nastavi_premijo('letno')
##Zavarovanje2.ustvari_zavarovanje()
##Domen = Stranka('Kaj', 'Delas', 40)
##Zavarovanje2= Nezgodno_zavarovanje(10, 'velik')
##Zavarovanje2.nastavi_lastnika(Domen)
##Zavarovanje2.nastavi_premijo('letno')
##Zavarovanje2.ustvari_zavarovanje()
