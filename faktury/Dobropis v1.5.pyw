import tkFileDialog
from Tkinter import *
from dialog import dialog
from getpass import getuser
from ttk import Label, Button, Entry

def vyber():
    global data, tlacidlo, root
    name=tkFileDialog.askopenfilename()
    with file(name,"r") as subor:
        data=subor.read()
    tlacidlo.configure(text="Uprav faktury", command=spracuj)
    Label(root, text="Subor "+name.split("/")[-1]+" najdeny").grid(columnspan=2, row=4)

def spracuj():
    global cislo_faktury, cislo_faktury_entry,predfaktura,root
    cislo_faktury=cislo_faktury_entry.get()
    if len(cislo_faktury)<6:
        dialog(sprava="Kratke cislo faktury !")
    else:
        predfaktura=predfaktura.get()
        root.destroy()

root = Tk()
root.title("Dobropis v1.7 (c) rubint.sk")

Label(root, text="Cislo Faktury:").grid(column=0, row=0)
cislo_faktury_entry=Entry(root)
cislo_faktury_entry.grid(column=1, row=0)

Label(root, text="Zaplatena suma:").grid(column=0, row=1)
predfaktura=Entry(root)
predfaktura.grid(column=1, row=1)

tlacidlo=Button(root, text="Vyber faktury", command=vyber)
tlacidlo.grid(columnspan=2, row=5, sticky="nwes")

root.mainloop()

data=data.split("stream")
nove_faktury=""

nenasiel=True
for faktura in data:
    if cislo_faktury in faktura:
        try:
            try:
                stara_celkova=float(faktura.split("Spolu DPH")[1].split("Tm (")[2].split(") Tj")[0])
            except:
                stara_celkova=float(faktura.split("Total TVA")[1].split("Tm (")[2].split(") Tj")[0])
            nova_celkova=stara_celkova-float(predfaktura)
            
            faktura=faktura.replace("%.2f"%stara_celkova,"%.2f"%nova_celkova)
            rozdelena=faktura.split("""(ELETECHNIK s.r.o) Tj
0.00 0.00 0.00 rg""")
            faktura=rozdelena[0]+"""(ELETECHNIK s.r.o) Tj
0.00 0.00 0.00 rg
/F01 8 Tf
 1 0 0 1 40 88 Tm ( ) Tj
0.00 0.00 0.00 rg
/F01 8 Tf
 1 0 0 1 310 88 Tm (-%.2f) Tj
0.00 0.00 0.00 rg
/F01 8 Tf
 1 0 0 1 200 88 Tm (-%.2f) Tj
0.00 0.00 0.00 rg
/F00 8 Tf
 1 0 0 1 400 128 Tm (Spolu) Tj
0.00 0.00 0.00 rg
/F00 7 Tf
 1 0 0 1 400 105 Tm (%.2fEUR) Tj
0.00 0.00 0.00 rg
/F00 7 Tf
 1 0 0 1 397 92 Tm (-%.2fEUR) Tj
0.00 0.00 0.00 rg
/F00 7 Tf
 1 0 0 1 440 92 Tm (Preddavok) Tj
0.00 0.00 0.00 rg

"""%(float(predfaktura)-float(predfaktura)/1.2, float(predfaktura)/1.2, float(stara_celkova), float(predfaktura))+rozdelena[1]
            nove_faktury+=faktura+"stream"
            nenasiel=False  
        except IndexError as err:
            dialog("Chyba", "Neviem najst vo fakturach - zly format alebo faktura na viacej stran.\nAk sa nepodarilo vytvorit dobropis, kontaktujte spravcu(%s)"%err)
            nove_faktury+=faktura+"stream"
        except ValueError as err:
            if "Vsetok nas tovar je dopravovany na riziko a nebezpecie adresata" in str(err):
                nove_faktury+=faktura+"stream"
            else:
                dialog(" Chyba ",err)
    else:
        nove_faktury+=faktura+"stream"

try:
    with file("C:\\Users\\%s\\Desktop\\upravene.pdf"%getuser(),"w") as subor: subor.write(nove_faktury[:-7])
    dialog("Info", "nasiel som fakturu %s, povodna hodnota faktury %.2f\nHotovo !"%(cislo_faktury,stara_celkova))
except IOError as err:
    dialog("Chyba", 'Pozor, subor "upravene.pdf" otvoreny v inom programe (%s)'%err)    

if nenasiel:
    dialog("Chyba", "Neviem najst fakturu c.%d"%(int(cislo_faktury)))
    
