import subprocess, os, sys
import datetime
TRAJANJA = {1: 1, 5: 0.95, 10: 0.85}
PAKETI = {'velik': 200, 'majhen': 150}
ŠTEVILKE = '0123456789'

def DANAŠNJI_DATUM():
    return str(datetime.datetime.now())[8:10] + '.' + str(datetime.datetime.now())[5:7] + '.' + str(datetime.datetime.now())[:4]

def vsebuje_številke(niz):
    for i in ŠTEVILKE:
        if i in niz:
            return True
    return False

#funkcije da preverim če je datum rojstva veljaven
def prestopno(leto):
    return leto % 4 == 0 and leto % 100 != 0 or leto % 400 == 0

def stevilo_dni(mesec, leto):
    if mesec == 2 and prestopno(leto):
        return 29
    elif mesec == 2:
        return 28
    elif mesec == 4 or mesec == 6 or mesec == 9 or mesec == 11:
        return 30
    else:
        return 31

def je_veljaven_datum(dan, mesec, leto):
    for s in [dan, mesec, leto]:
        for c in s:
            if c not in ŠTEVILKE:
                return False
    dan = int(dan)
    mesec = int(mesec)
    leto = int(leto)
    return 1<= mesec <= 12 and 1 <= dan <= stevilo_dni(mesec, leto) and 1900 <= leto <= 2018
    
        
class Stranka:

    def __init__(self):
        self.ime = ''
        self.priimek = ''

    def __repr__(self):
        return 'Stranka({}, {}, {})'.format(self.ime, self.priimek, self.datum_rojstva)

    def __str__(self):
        return '{} {}, rojen/a: {}'.format(self.ime, self.priimek, self.datum_rojstva)

    def nastavi_ime_priimek_datum_rojstva(self, ime, priimek, datum_rojstva):
        self.ime = ime
        self.priimek = priimek
        self.datum_rojstva = datum_rojstva
        self.starost = int(DANAŠNJI_DATUM()[-4:]) - int(self.datum_rojstva[-4:])

    def ponastavi_podatke(self):
        self.ime = ''
        self.priimek = ''

class Nezgodno_zavarovanje:

    def __init__(self):
        self.trajanje = None
        self.paket = None
        self.premija = None

    def __str__(self):
        return 'Nezgodno zavarovanje št. {}, lastnik: {}'.format(self.številka, self.lastnik)

    def __repr__(self):
        return 'Nezgodno_zavarovanje({}, {})'.format(self.trajanje, self.paket)

    def nastavi_številko(self):
        #nastavi datum sklenitve in številko zavarovanja, ki je unikatna vsakemu zavarovanju
        self.datum_sklenitve = DANAŠNJI_DATUM()
        with open('številka_zavarovanja.txt') as dat:
            številka_zavarovanja = dat.readline()
        self.številka = številka_zavarovanja
        with open('številka_zavarovanja.txt', 'w') as dat:
            številka_zavarovanja_večja = int(self.številka) + 1
            številka_zavarovanja_string = str(številka_zavarovanja_večja).zfill(6)
            dat.write(številka_zavarovanja_string)

    def nastavi_trajanje(self, trajanje):
        self.trajanje = trajanje

    def nastavi_paket(self, paket):
        self.paket = paket

    def nastavi_lastnika(self, stranka):
        self.lastnik = stranka
    
    def nastavi_premijo(self, interval_plačevanja):
        #izračuna višino premije glede na starost stranke, trajanje in paket zavarovanja in izračuna kolikšno je mesečno/letno plačilo
        self.interval_plačevanja = interval_plačevanja
        if self.lastnik.starost >= 65:
            k = 1.2
        else:
            k = 1
        self.premija = TRAJANJA.get(self.trajanje) * k * PAKETI.get(self.paket) * self.trajanje
        if self.interval_plačevanja == 'mesečno':
            self.plačilo = self.premija / self.trajanje / 12
            return 'Vaše mesečno plačilo je {:.2f}'.format(self.plačilo)
        else:
            self.plačilo = self.premija / self.trajanje
            return 'Vaše letno plačilo je {:.2f}'.format(self.plačilo)

    def ustvari_zavarovanje(self):
        if self.premija == None: 
            pass #to sem dodala zato da ni težav pri gumbu ustvari zavarovanje v uporabniškem vmesniku
        else:
            #ustvari dat sklenjena zavarovanja oz. dodaj vanjo podatke o zavarovanju
            with open('sklenjena_zavarovanja.txt', 'a', encoding='latin2') as sklenjena_zavarovanja:
                sklenjena_zavarovanja.write('{}: Nezgodno zavarovanje, {}, {}, {}, {:.2f}, {} {}, {}\n'.format(self.številka, self.trajanje, self.paket, self.interval_plačevanja, self.premija, self.lastnik.ime, self.lastnik.priimek, self.datum_sklenitve))
            
            #ustvari datoteko baza oseb oz. dodaj vanjo podatke o stranki (če je to prvo sklenjeno zavarovanje te stranke) oz. dodaj št. zavarovanja k stranki (lastniku zavarovanja)
            with open('baza_oseb.txt', 'a', encoding='latin2') as baza_oseb:
                pass  #če datoteka še ne obstaja se ustvari tukaj
            with open('baza_oseb.txt', encoding='latin2') as baza_oseb:
                osebe = baza_oseb.readlines()
            lastnika_ni_v_bazi = True
            for i in range(len(osebe)):
                if osebe[i].startswith('{}, {}, {}'.format(self.lastnik.ime, self.lastnik.priimek, self.lastnik.datum_rojstva)):
                    osebe[i] = osebe[i].strip() + ', {}\n'.format(self.številka)
                    lastnika_ni_v_bazi = False
                    break
            if lastnika_ni_v_bazi:
                osebe += ['{}, {}, {}: {}\n'.format(self.lastnik.ime, self.lastnik.priimek, self.lastnik.datum_rojstva, self.številka)]
            with open('baza_oseb.txt', 'w', encoding='latin2') as baza_oseb:
                for vrstica in osebe:
                    baza_oseb.write(vrstica)

    def ustvari_dokument(self):
        #ustvari in odpre dokument (zavarovalno polico), ki ga naj bi ga zavarovalniški posrednik dal podpisati stranki
        with open('Nezgodno_zavarovanje_št_{}.txt'.format(self.številka), 'w', encoding='latin2') as doc:
            print('POLICA ZA NEZGODNO ZAVAROVANJE\n', file=doc)
            print('Polica št. {}\n'.format(self.številka), file=doc)
            print('PODATKI O ZAVAROVALCU/ ZAVAROVANCU', file=doc)
            print('Ime in priimek: {} {}'.format(self.lastnik.ime, self.lastnik.priimek), file=doc)
            print('Datum rojstva: {}\n'.format(self.lastnik.datum_rojstva), file=doc)
            print('PODATKI O ZAVAROVANJU', file=doc)
            print('Datum sklenitve: {}'.format(self.datum_sklenitve), file=doc)
            print('Trajanje: {} let{}'.format(self.trajanje, 'o' if self.trajanje == 1 else ''), file=doc)
            print('Paket: {}'.format(self.paket), file=doc)
            print('Osnovna letna premija: {:.2f} EUR'.format(self.premija / self.trajanje), file=doc)
            print('Dinamika plačevanja: {}'.format(self.interval_plačevanja), file=doc)
            print('{} premija: {:.2f} EUR\n'.format('Mesečna' if self.interval_plačevanja == 'mesečno' else 'Letna', self.plačilo), file=doc)
            print('ZAVAROVALNE VSOTE', file=doc)
            if self.paket == 'velik':
                print('Smrt: 20 000 EUR\nMesečna renta: 200 EUR\nInvalidnost:150 000 EUR\nNadomestilo za zlom kosti: 3000 EUR\n', file=doc)
            else:
                print('Smrt: 15 000 EUR\nMesečna renta: 100 EUR\nInvalidnost:100 000 EUR\n', file=doc)
            print('Zavarovanec potrjuje, da je prejel pogoje\nzavarovanja in je z njimi tudi seznanjen.\n', file=doc)
            print('Ljubljana, dne {}\n'.format(DANAŠNJI_DATUM()), file=doc)
            print('_________________________', file=doc)
        #ker so za različne sisteme potrebni različni ukazi za odpiranje datoteke sem vključila 3 možnosti: prva za apple, druga za windows in tretja za linux 
        if sys.platform == 'darwin':
            subprocess.call(['open','Nezgodno_zavarovanje_št_{}.txt'.format(self.številka)])
        elif sys.platform == 'win32':
            os.startfile('Nezgodno_zavarovanje_št_{}.txt'.format(self.številka))
        else:
            subprocess.call(['xdg-open','Nezgodno_zavarovanje_št_{}.txt'.format(self.številka)])

    def ponastavi_podatke(self):
        self.trajanje = None
        self.paket = None
        self.premija = None
