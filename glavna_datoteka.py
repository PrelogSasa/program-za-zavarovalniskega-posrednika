DANAŠNJI_DATUM = '5.7.2018'
#pogrunti kko dobit današnji datum


class Stranka:
    def __init__(self, ime, priimek, datum_rojstva):
        self.ime = ime
        self.priimek = priimek
        self.datum_rojstva = datum_rojstva
        self.starost = int(DANAŠNJI_DATUM[-4:]) - int(self.datum_rojstva[-4:])
        

    def __repr__(self):
        return 'Stranka({}, {}, {})'.format(self.ime, self.priimek, self.datum_rojstva)

    def __str__(self):
        return '{} {}, rojen/a: {}'.format(self.ime, self.priimek, self.datum_rojstva)


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
        #ustvari oz. dodaj v datoteko sklenjena zavarovanje
        with open('sklenjena_zavarovanja.txt', 'a') as sklenjena_zavarovanja:
            sklenjena_zavarovanja.write('{}: Nezgodno zavarovanje, {}, {}, {}, {} {}\n'.format(self.številka, self.trajanje, self.paket, self.premija, self.lastnik.ime, self.lastnik.priimek))
        
        #ustvari novo oz. dodaj v bazo oseb
        with open('baza_oseb.txt', 'a') as baza_oseb:
            pass
        with open('baza_oseb.txt') as baza_oseb:
            osebe = baza_oseb.readlines()
        lastnika_ni_v_bazi = True
        for i in range(len(osebe)):
            if osebe[i].startswith('{}, {}, {}'.format(self.lastnik.ime, self.lastnik.priimek, self.lastnik.datum_rojstva)):
                osebe[i] = osebe[i].strip() + ', {}\n'.format(self.številka)
                lastnika_ni_v_bazi = False
                break
        if lastnika_ni_v_bazi:
            osebe += ['{}, {}, {}: {}\n'.format(self.lastnik.ime, self.lastnik.priimek, self.lastnik.datum_rojstva, self.številka)]
        with open('baza_oseb.txt', 'w') as baza_oseb:
            for vrstica in osebe:
                baza_oseb.write(vrstica)

    def ustvari_dokument(self):
        with open('Nezgodno_zavarovanje_št_{}.txt'.format(self.številka), 'w') as doc:
            print('POLICA ZA NEZGODNO ZAVAROVANJE\n', file=doc)
            print('Polica št. {}\n'.format(self.številka), file=doc)
            print('PODATKI O ZAVAROVALCU/ ZAVAROVANCU', file=doc)
            print('Ime in priimek: {} {}'.format(self.lastnik.ime, self.lastnik.priimek), file=doc)
            print('Datum rojstva: {}'.format(self.lastnik.datum_rojstva), file=doc)
            
            
            
            

##Maja = Stranka('Vladimir', 'Putin', '6.6.1965')
##Zavarovanje2= Nezgodno_zavarovanje(10, 'velik')
##Zavarovanje2.nastavi_lastnika(Maja)
##Zavarovanje2.nastavi_premijo('letno')
##Zavarovanje2.ustvari_zavarovanje()
##Domen = Stranka('Vladimir', 'Putin', '6.6.1965')
##Zavarovanje2= Nezgodno_zavarovanje(10, 'majhen')
##Zavarovanje2.nastavi_lastnika(Domen)
##Zavarovanje2.nastavi_premijo('letno')
##Zavarovanje2.ustvari_zavarovanje()
