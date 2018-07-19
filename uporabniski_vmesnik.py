import tkinter as tk
from glavna_datoteka import *

NZ = Nezgodno_zavarovanje()
OS = Stranka()

def naslednja_stran(stran):
    stran.tkraise()

okno = tk.Tk()
okno.geometry('500x500')
okno.resizable(0, 0)

stran1 = tk.Frame(okno)
stran2 = tk.Frame(okno)
stran3 = tk.Frame(okno)
stran4 = tk.Frame(okno)
stran5 = tk.Frame(okno)

for stran in [stran1, stran2, stran3, stran4, stran5]:
    stran.grid(row=0, column=0, sticky='NEWS')
 #   stran.pack_propagate(0)
    

#stran1    
tk.Button(stran1, text='Skleni novo nezgodno zavarovanje', command=lambda:naslednja_stran(stran2) and NZ.nastavi_številko()).pack()

#stran 2
var1 = tk.IntVar()   
tk.Label(stran2, text='Trajanje nezgodnega zavarovanja:').pack()
tk.Radiobutton(stran2, text='1 leto', variable=var1, value=1, command=lambda:NZ.nastavi_trajanje(1)).pack()
tk.Radiobutton(stran2, text='5 let', variable=var1, value=5, command=lambda:NZ.nastavi_trajanje(5)).pack()
tk.Radiobutton(stran2, text='10 let', variable=var1, value=10, command=lambda:NZ.nastavi_trajanje(10)).pack()

var2 = tk.StringVar()
tk.Label(stran2, text='Paket nezgodnega zavarovanja:').pack()
tk.Radiobutton(stran2, text='majhen', variable=var2, value='majhen', command=lambda:NZ.nastavi_paket('majhen')).pack()
tk.Radiobutton(stran2, text='velik', variable=var2, value='velik', command=lambda:NZ.nastavi_paket('velik')).pack()

tk.Button(stran2, text='Naslednja stran >>', command=lambda:naslednja_stran(stran3)).pack(side=tk.BOTTOM)

#stran 3
tk.Label(stran3, text='PODATKI O STRANKI').grid(column=0, row=0)
tk.Label(stran3, text='Ime:').grid(column=0, row=1)
ime = tk.Entry(stran3, textvariable=tk.StringVar())
ime.grid(column=1, row=1, columnspan=3)
tk.Label(stran3, text='Priimek:').grid(column=0, row=2)
priimek = tk.Entry(stran3, textvariable=tk.StringVar())
priimek.grid(column=1, row=2, columnspan=3)
tk.Label(stran3, text='Datum rojstva:').grid(column=0, row=3)
dan = tk.Spinbox(stran3, from_=1, to=31, width=6)
dan.grid(column=1, row=3)
mesec = tk.Spinbox(stran3, from_=1, to=12, width=6)
mesec.grid(column=2, row=3)
leto = tk.Spinbox(stran3, from_=1900, to=2018, width=7)
leto.grid(column=3, row=3)

naslednja_stran(stran1)
okno.mainloop()
