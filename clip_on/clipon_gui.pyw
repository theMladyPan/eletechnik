# -*- coding: cp1250 -*-
from time import sleep
from Tkinter import *
from ttk import *
from thread import start_new_thread as thread
import pickle, sys, time, os, ctypes, urllib2
from SendKeys import SendKeys
from subprocess import call, Popen, PIPE

def paste():
    ctypes.windll.user32.OpenClipboard(0)
    pcontents = ctypes.windll.user32.GetClipboardData(1) # 1 is CF_TEXT
    data = ctypes.c_char_p(pcontents).value
    #ctypes.windll.kernel32.GlobalUnlock(pcontents)
    ctypes.windll.user32.CloseClipboard()
    return data

def copy(text):
    text = str(text)
    GMEM_DDESHARE = 0x2000
    ctypes.windll.user32.OpenClipboard(0)
    ctypes.windll.user32.EmptyClipboard()
    hCd = ctypes.windll.kernel32.GlobalAlloc(GMEM_DDESHARE, len(bytes(text))+1)
    pchData = ctypes.windll.kernel32.GlobalLock(hCd)
    ctypes.cdll.msvcrt.strcpy(ctypes.c_char_p(pchData), bytes(text))
    ctypes.windll.kernel32.GlobalUnlock(hCd)
    ctypes.windll.user32.SetClipboardData(1, hCd)
    ctypes.windll.user32.CloseClipboard()

def send(arg):
    SendKeys(arg, turn_off_numlock=False,pause=0.01)

class errFrame:
    def write(self, text):
        okno=Toplevel()
        Label(okno, text=str(text)).pack()
        okno.mainloop()
class Main:
    def __init__(self):
        sys.stdout=errFrame()
        self.main=Tk()
        self.main.title("klip v1.6.0")
        self.main.iconbitmap(bitmap = "ico.ico")
        self.main.protocol("WM_DELETE_WINDOW", self.on_destroy)
        self.vars=[]
        self.filtruj=IntVar()
        self.nahod=IntVar()
        self.nahod_cde=IntVar()
        self.stary_klip=paste()
        self.dokumentacia=IntVar()

        with open("\\\\servag60\\UTILISATEURS\\fichierscommun\\!!!SOFT\\python\\admall\\refs.db", "r") as subor:
            self.referencie=subor.read().split("\n")

        try:
            with open("filtruj.defaults","r") as subor:
                self.filtruj.set(int(subor.read()))
        except: pass

        self.opts={"medzera":" ","pomlcka":"-",
                   "podtrznik":"_","novy riadok":"\n",
                   "navrat kurzora":"\r","lomitko":"/",
                   "tabulator":"	", "ciarka":",",
                   "bodka":"."}
        
        for i in range(len(self.opts.keys())):
                self.vars.append(IntVar())

        try:
            with open("vars.defaults","r") as subor:
                data=subor.read()
                for i in range(len(self.vars)):
                    self.vars[i].set(int(data[i]))
        except:
            pass
        
        Label(self.main, text=u"Odstráň:").grid(row=0, column=0)
        self.checkboxes=[]
        
        for i in range(len(self.opts.keys())):
            self.checkboxes.append(Checkbutton(self.main, variable=self.vars[i],onvalue=1, offvalue=0))
            self.checkboxes[i].grid(column=0, row=i+1)
            Label(self.main, text=self.opts.keys()[i])\
                             .grid(row=i+1, column=1, sticky="W")
        

        self.nahrada=Frame(self.main)
        self.nahrada.grid(row=18, columnspan=3, sticky="WENS")

        self.co=Entry(self.nahrada, width=4)
        self.co.grid(column=0, row=0)

        Label(self.nahrada, text="=>").grid(column=1, row=0, sticky="WENS")
        
        self.cim=Entry(self.nahrada, width=15)
        self.cim.grid(column=2, row=0, sticky="WENS")
        
        Label(self.nahrada, text="Prefix").grid(row=1, column=0)
        self.prefix=Entry(self.nahrada, width=15)
        self.prefix.grid(row=1, column=2, sticky="W")

        try:
            with open("prefix.defaults","r") as subor:
                self.prefix.insert(0,subor.read())
        except: pass
        
        Checkbutton(self.main, variable=self.filtruj, onvalue=1, offvalue=0).grid(column=0, row=20)
        Label(self.main, text="Filtruj").grid(column=1,row=20, columnspan=2, sticky="W")
        Checkbutton(self.main, variable=self.nahod, onvalue=1, offvalue=0).grid(column=0, row=21)
        Label(self.main, text="Pridaj do tarifu").grid(column=1,row=21, columnspan=2, sticky="W")
        Checkbutton(self.main, variable=self.nahod_cde, onvalue=1, offvalue=0).grid(column=0, row=22)
        Label(self.main, text="Pridaj do CDE").grid(column=1,row=22, columnspan=2, sticky="W")
        #Checkbutton(self.main, variable=self.dokumentacia, onvalue=1, offvalue=0, state="disabled").grid(column=0, row=23)
        #Label(self.main, text="Zamen dokuemntaciou").grid(column=1,row=23, columnspan=2, sticky="W")

        thread(self.scan, ())
        self.main.bind("f", self.switch)
        self.main.bind("<Escape>", self.iconify)
        self.main.mainloop()

    def iconify(self, key=0):
        self.main.iconify()

    def switch(self, key=0):
        if self.filtruj.get():
            self.filtruj.set(0)
        else:
            self.filtruj.set(1)
        
    def scan(self):
        while self.main:
            if self.filtruj.get():
                retazec=""
                for i in range(len(self.opts.keys())):
                    if self.vars[i].get():
                        retazec=retazec+ self.opts[self.opts.keys()[i]]
                klip=paste()
                try: klip.replace("","")
                except: continue  
                for i in retazec:
                    klip=klip.replace(i,"")
                klip=klip.replace(self.co.get(),self.cim.get())
                if self.prefix.get() not in klip:
                    if "EAT" in self.prefix.get():
                        klip=("EAT"+('0'*(9-len(klip)))+klip)
                    else:
                        klip=self.prefix.get()+klip
                if self.stary_klip != paste():
                    copy(klip)
                    if self.nahod.get():
                        self.pridaj_do_tarifu()
                    if self.nahod_cde.get():
                        self.pridaj_do_cde()
                    if self.dokumentacia.get():
                        self.zamen_dokumentaciou()
                        
                self.stary_klip=klip
            sleep(0.2)

    def pridaj_do_tarifu(self):
        os.system("C:\gesco5\\taroffre.exe")
        send("{ESC}{INSERT}1{ENTER}")
        send("^v")
        send("{ENTER}"*9)
        
    def pridaj_do_cde(self):
        os.system("C:\gesco5\\client_cde.exe")
        send("{ESC}{INSERT}1{ENTER}")
        send("^v")
        if "WOH" in paste():
            response = urllib2.urlopen('http://pim.woehner.de/online/cms/EN/US/catalog/metallzuschlaege?artikel=%s&discount=63'%(paste().replace("WOH","")))
            html = response.read().replace("	","").replace("\n","")
            html=html.split("""<td>Final price per piece</td><td class="cell-align-right">""")
            html=html[1].split("</td>")
            nakup=html[0]

            send("{ENTER}"*11)
            send(nakup)
            send("{ENTER}"*9)
            
        else:
            send("{ENTER}"*9)
                
    def on_destroy(self):
        with open("vars.defaults","w") as subor:
            data=""
            for i in range(len(self.vars)):
                data+=str(self.vars[i].get())
            subor.write(data)
            
        with open("filtruj.defaults","w") as subor:
                subor.write(str(self.filtruj.get()))

        with open("prefix.defaults","w") as subor:
                subor.write(str(self.prefix.get()))
        
        self.main.destroy()
        self.main=False

if __name__ == "__main__":
    Main()
