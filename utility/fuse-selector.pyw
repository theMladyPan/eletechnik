from Tkinter import Tk, StringVar
from ttk import Entry, Combobox, Button
import webbrowser

def open_ad():
    webbrowser.open("https://mall.industry.siemens.com/mall/en/sk/Catalog/Product/%s"%total_var.get())
    
def istiaca_schopnost_eval(event):
    if istiaca_schopnost.current() == 0:
        ist_sch.set("5SL6")
    if istiaca_schopnost.current() == 1:
        ist_sch.set("5SY4")
    if istiaca_schopnost.current() == 2:
        ist_sch.set("5SY7")
    if istiaca_schopnost.current() == 3:
        ist_sch.set("5SY8")
    total_var.set(ist_sch.get()+pol_var.get()+amp_var.get()+char_var.get())
        
def poly_eval(event):
    if poly.current() == 0:
        pol_var.set("1")
    if poly.current() == 1:
        pol_var.set("5")
    if poly.current() == 2:
        pol_var.set("2")
    if poly.current() == 3:
        pol_var.set("3")
    if poly.current() == 4:
        pol_var.set("6")
    if poly.current() == 5:
        pol_var.set("4")
    total_var.set(ist_sch.get()+pol_var.get()+amp_var.get()+char_var.get())

def ampere_eval(event):
    if ampere.current() == 0:
        amp_var.set("14")
    if ampere.current() == 1:
        amp_var.set("05")
    if ampere.current() == 2:
        amp_var.set("01")
    if ampere.current() == 3:
        amp_var.set("15")
    if ampere.current() == 4:
        amp_var.set("02")
    if ampere.current() == 5:
        amp_var.set("03")
    if ampere.current() == 6:
        amp_var.set("04")
    if ampere.current() == 7:
        amp_var.set("11")
    if ampere.current() == 8:
        amp_var.set("06")
    if ampere.current() == 9:
        amp_var.set("08")
    if ampere.current() == 10:
        amp_var.set("10")
    if ampere.current() == 11:
        amp_var.set("13")
    if ampere.current() == 12:
        amp_var.set("18")
    if ampere.current() == 13:
        amp_var.set("16")
    if ampere.current() == 14:
        amp_var.set("20")
    if ampere.current() == 15:
        amp_var.set("25")
    if ampere.current() == 16:
        amp_var.set("30")
    if ampere.current() == 17:
        amp_var.set("32")
    if ampere.current() == 18:
        amp_var.set("35")
    if ampere.current() == 19:
        amp_var.set("40")
    if ampere.current() == 20:
        amp_var.set("45")
    if ampere.current() == 21:
        amp_var.set("50")
    if ampere.current() == 22:
        amp_var.set("60")
    if ampere.current() == 23:
        amp_var.set("63")
    if ampere.current() == 24:
        amp_var.set("80")
    total_var.set(ist_sch.get()+pol_var.get()+amp_var.get()+char_var.get())

def char_eval(event):
    if char.current() == 0:
        char_var.set("-5")
    if char.current() == 1:
        char_var.set("-6")
    if char.current() == 2:
        char_var.set("-7")
    if char.current() == 3:
        char_var.set("-8")
    total_var.set(ist_sch.get()+pol_var.get()+amp_var.get()+char_var.get())
      
hl=Tk()
hl.title("Siemens MCB selector")

ist_sch=StringVar()
char_var=StringVar()
amp_var=StringVar()
pol_var=StringVar()
total_var=StringVar()

istiaca_schopnost=Combobox(hl, width=5, state='readonly')
istiaca_schopnost.bind("<<ComboboxSelected>>", istiaca_schopnost_eval)
istiaca_schopnost['values']=("6kA", "10kA", "15kA", "25kA")
istiaca_schopnost.current(1)
istiaca_schopnost.grid(row=1, column=6)
ist_sch.set("5SY4")

poly=Combobox(hl, width=5, state='readonly')
poly.bind("<<ComboboxSelected>>", poly_eval)
poly['values']=("1P", "1P+N", "2P", "3P", "3P+N","4P")
poly.current(0)
poly.grid(row=1, column=7)
pol_var.set("1")

ampere=Combobox(hl, width=4, state='readonly')
ampere.bind("<<ComboboxSelected>>", ampere_eval)
ampere['values']=("0.3A", "0.5A", "1A", "1.6A", "2A","3A","4A","5A","6A","8A","10A","13A","15A","16A","20A","25A","30A","32A","35A","40A","45","50A","60A","63A","80A")
ampere.current(8)
ampere.grid(row=1, column=8)
amp_var.set("06")

char=Combobox(hl, width=2, state='readonly')
char.bind("<<ComboboxSelected>>", char_eval)
char['values']=("A","B","C","D")
char.current(2)
char.grid(row=1, column=9)
char_var.set("-7")

Button(hl, text="Check A&D", command=open_ad).grid(row=1, column=10, sticky="WENS")

total_var.set(ist_sch.get()+pol_var.get()+amp_var.get()+char_var.get())
Entry(hl, textvariable=total_var, width=12).grid(row=1, column=1)

hl.mainloop()
