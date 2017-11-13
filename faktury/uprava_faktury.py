try:
    with file("original.pdf","r") as subor:
        data=subor.read()
except:
    raw_input("V priecinku sa nenachadza subor original.pdf. Koncim.")
    exit(0)

data=data.split("stream")
nove_faktury=""
cislo_faktury=raw_input("Zadaj cislo faktury: ")
predfaktura=raw_input("Zadaj sumu zaplatenej predfaktury: ")
stara_celkova=raw_input("Povodna celkova hodnota na zaplatenie: ")
nova_celkova=raw_input("Nova celkova hodnota na zaplatenie: ")

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
    
