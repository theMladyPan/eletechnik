# -*- coding: cp1250 -*-
from PyPDF2 import PdfFileWriter, PdfFileReader
from Tkinter import Tk
import os, codecs, time, tkFileDialog

for i in os.listdir("faktury"):
    os.remove("faktury\\"+i)

subory=os.listdir("\\\SERVEURAG60\\gesco\\dbase\\BL\\facturation")
pdfka=[]
posledna=0

for i in subory:
    if ".pdf" in i and "ORIGINALES" in i:
        #print int(i.split("_")[2])
        if int(i.split("_")[2]) > posledna:
            posledna=int(i.split("_")[2])
            cFA=i.split("_")[2]

FA= "factures_060_%s_ORIGINALES.pdf"%cFA

#okno=Tk()
#input1 = PdfFileReader(open(tkFileDialog.askopenfilename(), "rb"))
#okno.destroy()

input1 = PdfFileReader(open("\\\SERVEURAG60\\gesco\\dbase\\BL\\facturation\\"+FA, "rb"))

pages=input1.getNumPages()
pocet_stran_fakturacie=pages
pocet_stran_rozhodenych=0
zvysok=[]

for i in range(pages):
    zvysok.append(input1.getPage(i))

with open("klienti.txt","rb") as subor:
    klienti=subor.read().split("\n")

pocet_klientov=len(klienti)

#pre kazdeho klienta
for klient in klienti:
    os.system("cls")
    print u"Vitajte!\n(c) Rubint.sk 2016\n\nExtrahujem fakt�ry z %s: %s\n\n[%s%s] %d/%d str�n ost�va.\n\n" % (FA, unicode(klient, "ascii", "ignore").encode("ascii"), "#"*int(50*(klienti.index(klient)/float(pocet_klientov)))," "*int(50*((pocet_klientov-klienti.index(klient))/float(pocet_klientov))),pocet_stran_fakturacie - pocet_stran_rozhodenych, pocet_stran_fakturacie)


    output = PdfFileWriter()
    su_faktury=False
    zvysok.reverse()
    strany=zvysok
    zvysok=[]

    while strany:
        page=strany.pop()

        if unicode(klient,"cp1250").replace("\r","") in page.extractText():
            text= page.extractText()
            if "TVA Intra" in text:
                print "FA: ",text.split("TVA Intra")[0][-6:],"-", klient
            else:
                print "FA: ",text.split("ICDPH")[0][-6:],"-", klient
            su_faktury = True
            output.addPage(page)
            pocet_stran_rozhodenych+=1

        else:
            zvysok.append(page)
    if su_faktury:
        outputStream = file("faktury\\FA_"+unicode(klient,"ascii","ignore").encode("ascii").replace("\r","")+".pdf", "wb")
        output.write(outputStream)
        outputStream.close()

#faktury na vytlacenie
output = PdfFileWriter()
zvysok.reverse()
strany=zvysok
zvysok=[]
mnozstvo=len(strany)

while strany:
    os.system("cls")
    print u"\n\n Hotovo, extrahujem faktury na vytla�enie:\n\n[%s%s] %d/%d str�n ost�va.\n\n"%("#"*int(50*(len(strany)/float(mnozstvo)))," "*int(50*((mnozstvo-len(strany))/float(mnozstvo))),pocet_stran_fakturacie - pocet_stran_rozhodenych, pocet_stran_fakturacie)
    page=strany.pop()
    output.addPage(page)
    pocet_stran_rozhodenych+=1
outputStream = file("faktury\\FA_NA_VYTLACENIE.pdf", "wb")
output.write(outputStream)
outputStream.close()


#najdi faktury tzv. Obj. pride

output = PdfFileWriter()
su_faktury=False

for i in range(pages):
    os.system("cls")
    print u"\n\n Hotovo, extrahujem faktury bez objednavky:\n\n[%s%s] %d/%d str�n ost�va.\n\n"%("#"*int(50*(i/float(pages)))," "*int(50*((pages-i)/float(pages))),pages - i, pages )
    page=input1.getPage(i)

    if unicode("Obj. pride","cp1250").replace("\r","") in page.extractText():
        text= page.extractText()
        if "TVA Intra" in text:
            print "FA: ",text.split("TVA Intra")[0][-6:],"-", "Obj. pride"
        else:
            print "FA: ",text.split("ICDPH")[0][-6:],"-", "Obj. pride"
        su_faktury = True
        output.addPage(page)

if su_faktury:
    outputStream = file("faktury\\FA_"+unicode("obj_bez_FA","ascii","ignore").encode("ascii").replace("\r","")+".pdf", "wb")
    output.write(outputStream)
    outputStream.close()

#koniec

os.system("cls")
print "Hotovo!"
if pocet_stran_rozhodenych == pocet_stran_fakturacie:
    print u"Kr��ov� kontrola prebehla �spe�ne, str�n dokopy=%d"%pocet_stran_fakturacie
else:
    print u"POZOR! Kr��ov� kontrola neprebehla �spe�ne, po�et str�n sa l��i!"

raw_input("Enter...")
