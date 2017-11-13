# -*- coding: cp1250 -*-
from PyPDF2 import PdfFileWriter, PdfFileReader
from Tkinter import Tk
import os, codecs, time, tkFileDialog

for i in os.listdir("faktury"):
    os.remove("faktury\\"+i)

okno=Tk()
input1 = PdfFileReader(open(tkFileDialog.askopenfilename(), "rb"))
okno.destroy()


pages=input1.getNumPages()

with open("klienti.txt","rb") as subor:
    klienti=subor.read().split("\n")
    
pocet_klientov=len(klienti)

#pre kazdeho klienta 
for klient in klienti:
    os.system("cls")
    print u"Vitajte!\n\nExtrahujem faktúry: %s\n\n[%s%s]\n\n" % (unicode(klient, "ascii", "ignore").encode("ascii"), "#"*int(70*(klienti.index(klient)/float(pocet_klientov)))," "*int(70*((pocet_klientov-klienti.index(klient))/float(pocet_klientov))))
                                        

    output = PdfFileWriter()
    su_faktury=False
    
    for i in range(pages):
        page=input1.getPage(i)
        
        if unicode(klient,"cp1250").replace("\r","") in page.extractText():
            text= page.extractText()
            if "TVA Intra" in text:
                print "FA: ",text.split("TVA Intra")[0][-6:],"-", klient
            else:
                print "FA: ",text.split("ICDPH")[0][-6:],"-", klient
            su_faktury = True
            output.addPage(page)

    if su_faktury:
        outputStream = file("faktury\\FA_"+unicode(klient,"ascii","ignore").encode("ascii").replace("\r","")+".pdf", "wb")
        output.write(outputStream)
        outputStream.close()

#najdi faktury tzv. Obj. pride        

output = PdfFileWriter()
su_faktury=False
    
for i in range(pages):
    os.system("cls")
    print "\n\n Hotovo, extrahujem faktury bez objednavky:\n\n[%s%s]\n\n"%("#"*int(70*(i/float(pages)))," "*int(70*((pages-i)/float(pages))))
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
        
print "Hotovo!"
time.sleep(1)
