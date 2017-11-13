import pyperclip, os
from time import sleep
from SendKeys import SendKeys

debug=input("Debug? (0/1): ")

def send(arg):
    SendKeys(arg, turn_off_numlock=False,pause=0.05+0.2*debug)

kolko=input("Pocet poloziek: ")

os.startfile("C:\gesco5\\taroffre.exe")
sleep(1)

for i in range(kolko):
    if i=="":continue
    print "%d/%d"%(i,kolko)
    
    send("{ENTER}")
    send("%p")
    send("{DOWN}")
    send("%v")
    
    send("{ENTER}")
    send("{ESC}")
    send("{DOWN}")
