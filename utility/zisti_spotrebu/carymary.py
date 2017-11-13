with open("data.csv","r") as subor:
    data=subor.read()

referencie=[]
for riadok in data.split(chr(10)):
    try:
        referencia=riadok.split(chr(9))[3]
        if referencia not in referencie:
            referencie.append(referencia)
        else: pass
    except IndexError: pass

print "Referencia	Pocet objednavok	Median objednavok	Spolu objednanych"
for referencia in referencie:
    qty=[]
    for riadok in data.split(chr(10)):
        if referencia in riadok:
            qty.append(int(riadok.split(chr(9))[2]))
    qty.sort()
    try:
        print referencia,chr(9), data.count(referencia), chr(9),qty[len(qty)/2],chr(9),sum(qty), chr(9), qty
    except:
        print "pozor chyba!", qty
