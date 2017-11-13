import tkFileDialog
from Tkinter import *

def vyber():
    global data, tlacidlo, root
    name=tkFileDialog.askopenfilename()
    with file(name,"r") as subor:
        data=subor.read()
    tlacidlo.configure(text="Uprav faktury", command=spracuj)
    Label(root, text="Faktura "+name.split("/")[-1]+" najdena").grid(columnspan=2, row=4)

def spracuj():
    global cislo_faktury,predfaktura,stara_celkova,nova_celkova,root
    cislo_faktury=cislo_faktury.get()
    predfaktura=predfaktura.get()
    stara_celkova=stara_celkova.get()
    nova_celkova=nova_celkova.get()
    root.destroy()

root = Tk()
root.title("Fakturky v1.0")

Label(root, text="Cislo Faktury:").grid(column=0, row=0)
cislo_faktury=Entry(root)
cislo_faktury.grid(column=1, row=0)

Label(root, text="Zaplatena suma:").grid(column=0, row=1)
predfaktura=Entry(root)
predfaktura.grid(column=1, row=1)

Label(root, text="Povodna hodnota faktury:").grid(column=0, row=2)
stara_celkova=Entry(root)
stara_celkova.grid(column=1, row=2)

Label(root, text="Nova hodnota faktury:").grid(column=0, row=3)
nova_celkova=Entry(root)
nova_celkova.grid(column=1, row=3)

tlacidlo=Button(root, text="Vyber faktury", command=vyber)
tlacidlo.grid(columnspan=2, row=5, sticky="nwes")

root.mainloop()

data=data.split("stream")
nove_faktury=""

for faktura in data:
    if cislo_faktury in faktura:
        print "nasiel som fakturu %s"%cislo_faktury
        faktura=faktura.replace(stara_celkova,nova_celkova)
        rozdelena=faktura.split("""/F00 20 Tf
 1 0 0 1 34 794 Tm (ELETECHNIK s.r.o) Tj
0.00 0.00 0.00 rg""")
        faktura=rozdelena[0]+"""/F00 20 Tf
 1 0 0 1 34 794 Tm (ELETECHNIK s.r.o) Tj
0.00 0.00 0.00 rg
/F01 8 Tf
 1 0 0 1 40 88 Tm (-%s) Tj
0.00 0.00 0.00 rg
/F01 8 Tf
 1 0 0 1 305 88 Tm (-%.2f) Tj
0.00 0.00 0.00 rg
/F01 8 Tf
 1 0 0 1 200 88 Tm (-%s) Tj
0.00 0.00 0.00 rg"""%(predfaktura, float(predfaktura)*0.2, predfaktura)+rozdelena[1]
        nove_faktury+=faktura+"stream"
        
    else:
        nove_faktury+=faktura+"stream"

with file("upravene.pdf","w") as subor:
    subor.write(nove_faktury[:-7])
    
