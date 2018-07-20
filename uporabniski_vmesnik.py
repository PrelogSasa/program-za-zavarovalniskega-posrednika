import tkinter
from tkinter import Tk, Frame, Button, Label, Radiobutton, IntVar, StringVar, BOTTOM, Entry, Spinbox, messagebox, RAISED
from glavna_datoteka import *

NZ = Nezgodno_zavarovanje() #ustvarim objekt za nezgodno zavarovanje in mu skozi uporabniški vmesnik dodajam atribute
OS = Stranka() # ustvarim objekt stranka in ji skozi uporabniški vmesnik dodajam atribute

#različne strani (z različnimi gumbi) prikažem tako, da je vsaka stran en Frame in vsi so drug nad drugim in ko želim prikazati naslednjo stran dvignem ustrezen Frame na vrh.
def naslednja_stran(stran):
    if stran == stran3 and (NZ.trajanje == None or NZ.paket == None):
        messagebox.showerror('Napaka', 'Preden lahko nadaljujete morate izbrati trajanje in paket zavarovanja!')
    elif stran == stran4 and (OS.ime == '' or OS.priimek == ''):
        messagebox.showerror('Napaka', 'Preden lahko nadaljujete morate izpolniti vsa polja in pritisniti gumb Shrani!')
    elif stran == stran4 and (vsebuje_številke(OS.ime) or vsebuje_številke(OS.priimek)):
        messagebox.showerror('Napaka', 'Ime in priimek ne moreta vsebovati številk. Preden lahko nadaljujete morate popraviti in znova shraniti podatke o stranki!')
    elif stran == stran5 and NZ.premija == None:
        messagebox.showerror('Napaka', 'Preden lahko nadaljujete morate izbrati dinamiko plačevanja in pritisniti gumb Izračunaj!')
    else:
        stran.tkraise()
        a.deselect() # za stran 2
        b.deselect()
        c.deselect()
        k.deselect()
        l.deselect()
        ime.delete(0, last=20) # za stran 3
        priimek.delete(0, last=20)
        dan.delete(0, last=2)
        mesec.delete(0, last=2)
        leto.delete(0, last=4)
        m.deselect() # za stran 4
        n.deselect()
        izpis.config(text='')

#funkcija za gumb Shrani na strani 3
def shrani():
    if not je_veljaven_datum(dan.get(), mesec.get(), leto.get()):
        messagebox.showerror('Napaka', 'Vpisali ste neveljaven datum! Prosim vpišite veljaven datum v pravilna polja na način: dan s številko v prvo polje, mesec s številko v drugo polje, leto s številko v tretje polje.')
    else:
        OS.nastavi_ime_priimek_datum_rojstva(ime.get(), priimek.get(), dan.get().zfill(2) + '.' + mesec.get().zfill(2) + '.' + leto.get())
        


okno = Tk()
okno.geometry('500x250')
okno.resizable(0, 0)
okno.title('Program za zavarovalniškega posrednika')

stran1 = Frame(okno)
stran2 = Frame(okno)
stran3 = Frame(okno)
stran4 = Frame(okno)
stran5 = Frame(okno)

for stran in [stran1, stran2, stran3, stran4, stran5]:
    stran.grid(row=0, column=0, sticky='NEWS')
    

#stran1    
Button(stran1, text='Skleni novo nezgodno zavarovanje', command=lambda:[naslednja_stran(stran2), NZ.nastavi_številko()]).pack()

#stran 2 (zavarovanju nastavim atributa trajanje in paket)
var1 = IntVar()   #to poveže gumbe s to variable v eno skupino torej lahko izbereš samo enega izmed njih
Label(stran2, text='Trajanje nezgodnega zavarovanja:').pack()
a = Radiobutton(stran2, text='1 leto', variable=var1, value=1, command=lambda:NZ.nastavi_trajanje(1))
a.pack()
b = Radiobutton(stran2, text='5 let', variable=var1, value=5, command=lambda:NZ.nastavi_trajanje(5))
b.pack()
c = Radiobutton(stran2, text='10 let', variable=var1, value=10, command=lambda:NZ.nastavi_trajanje(10))
c.pack()

var2 = StringVar()
Label(stran2, text='Paket nezgodnega zavarovanja:').pack()
k = Radiobutton(stran2, text='majhen', variable=var2, value='majhen', command=lambda:NZ.nastavi_paket('majhen'))
k.pack()
l = Radiobutton(stran2, text='velik', variable=var2, value='velik', command=lambda:NZ.nastavi_paket('velik'))
l.pack()

Button(stran2, text='Naslednja stran >>', command=lambda:naslednja_stran(stran3)).pack(side=BOTTOM)

Button(stran2, text='Nazaj na glavni meni', command=lambda:[naslednja_stran(stran1), NZ.ponastavi_podatke()]).pack(side=BOTTOM)

#stran 3 (osebi nastavim atribute ime, priimek in datum rojstva, ter zavarovanju nastavim atribut lastnik)
Label(stran3, text='PODATKI O STRANKI').grid(column=0, row=0)

Label(stran3, text='Ime:').grid(column=0, row=1)
ime = Entry(stran3, textvariable=StringVar())
ime.grid(column=1, row=1, columnspan=3)

Label(stran3, text='Priimek:').grid(column=0, row=2)
priimek = Entry(stran3, textvariable=StringVar())
priimek.grid(column=1, row=2, columnspan=3)

Label(stran3, text='Datum rojstva:').grid(column=0, row=3)
dan = Entry(stran3, textvariable=StringVar(), width=6)
dan.grid(column=1, row=3)
mesec = Entry(stran3, textvariable=StringVar(), width=6)
mesec.grid(column=2, row=3)
leto = Entry(stran3, textvariable=StringVar(), width=7)
leto.grid(column=3, row=3)

Button(stran3, text='Shrani', command=lambda:shrani()).grid(column=2, row=4)

Button(stran3, text='Naslednja stran >>', command=lambda:[naslednja_stran(stran4), NZ.nastavi_lastnika(OS)]).grid(column=3, row=4)

Button(stran3, text='Nazaj na glavni meni', command=lambda:[naslednja_stran(stran1), NZ.ponastavi_podatke(), OS.ponastavi_podatke()]).grid(column=1, row=4)

#stran 4 (nastavi (in izračuna) atribute interval plačevanja, premija in mesečno/letno plačilo)
Label(stran4, text='Izberite dinamiko plačevanja:').pack()

var3 = StringVar()
m = Radiobutton(stran4, text='mesečno', variable=var3, value='mesečno')
m.pack()
n = Radiobutton(stran4, text='letno', variable=var3, value='letno')
n.pack()

Button(stran4, text='Izračunaj', command=lambda: izpis.config(text=NZ.nastavi_premijo(var3.get()))).pack()
izpis = Label(stran4)
izpis.pack()

Button(stran4, text='USTVARI ZAVAROVANJE', command=lambda:[naslednja_stran(stran5), NZ.ustvari_zavarovanje()]).pack(side=BOTTOM)

Button(stran4, text='Nazaj na glavni meni', command=lambda:[naslednja_stran(stran1), NZ.ponastavi_podatke(), OS.ponastavi_podatke()]).pack(side=BOTTOM)

#stran 5 (ustvari in odpre dokument(polico) zavarovanja)
Label(stran5, text='ZAVAROVANJE USPEŠNO USTVARJENO').pack()
Button(stran5, text='Prikaži zavarovalno polico', command=lambda:NZ.ustvari_dokument()).pack()

Button(stran5, text='Nazaj na glavni meni', command=lambda:[naslednja_stran(stran1), NZ.ponastavi_podatke(), OS.ponastavi_podatke()]).pack(side=BOTTOM)

naslednja_stran(stran1) #ko se aplikacija odpre se najprej pokaže prva stran
okno.mainloop()
