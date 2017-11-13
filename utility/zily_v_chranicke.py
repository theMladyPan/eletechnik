from Tkinter import Tk, StringVar
from ttk import Button, Entry, Label, Combobox

def pocitaj(*args):
    global pocet, main, plnenie

    vypocet = (((float(priemer.get())**2) *100* (int(pocet.get()))) / (((float(chranicka.get())/2)**2)*3.1416))
    
    if int(vypocet) > 70 and int(vypocet) <100:
        plnenie_entry.configure(foreground="#AA8800")
        plnenie.set("%.1f"%vypocet + " privela!")

    elif int(vypocet) >= 100:
        plnenie_entry.configure(foreground="#BB0000")
        plnenie.set("%.1f"%vypocet + " nezmesti sa!")
        
    else:
        plnenie_entry.configure(foreground="#00BB00")
        plnenie.set("%.1f"%vypocet + " v poriadku")
main=Tk()
main.title("Vypocet zil do chranicky v0.1")

Label(main, text="""Bezne priemery vodicov H07V-K:
prierez [mm2]	priemer [mm]
0,5		2,5
0,75		2,7
1		2,8
1,5		3,4
2,5		4,1
4		4,8
6		5,3
10		6,8""").grid(row=5, columnspan=3, sticky="WENS")

plnenie=StringVar()
plnenie.trace("w",pocitaj)

Label(main, text="Kolko zil: ").grid(row=0, column=0, sticky="WENS")
pocet=Entry(main)
pocet.insert(0, 10)
pocet.grid(row=0, column=1, sticky="WENS")

Label(main, text="Priemer zily: ").grid(row=1, column=0, sticky="WENS")
priemer=Entry(main)
priemer.insert(0, 3.4)
priemer.grid(row=1, column=1, sticky="WENS")
Label(main, text="mm").grid(row=1, column=2, sticky="WENS")

Label(main, text="Vnutorny priemer chranicky: ").grid(row=2, column=0, sticky="WENS")
chranicka=Entry(main)
chranicka.insert(0, 12.1)
chranicka.grid(row=2, column=1, sticky="WENS")
Label(main, text="mm").grid(row=2, column=2, sticky="WENS")

Label(main, text="Plnenie [%]: ").grid(row=3, column=0, sticky="WENS")
plnenie_entry=Entry(main, textvar=plnenie, state="disabled")
plnenie_entry.grid(row=3, column=1, sticky="WENS")

Button(main, text="Pocitaj!", command=pocitaj).grid(row=99, columnspan=20, sticky="WENS")

main.mainloop()
