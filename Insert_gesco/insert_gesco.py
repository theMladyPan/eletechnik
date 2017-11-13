import pyperclip, os
from time import sleep
from SendKeys import SendKeys

debug=input("Debug? (0/1): ")

def send(arg):
    SendKeys(arg, turn_off_numlock=False,pause=0.08*(debug+1))

data=pyperclip.paste()

os.startfile("C:\gesco5\\taroffre.exe")
sleep(1)

for i in data.split("\r\n"):
    if i=="":continue
    i=i.split("	")
    print "pridavam: ",i
    send("%n{ESC}{INSERT}")
    send(i[0])
    send("{ENTER}")
    send(i[1])
    send("{ENTER}")
    if len(i)>2:
        send(i[2]) 
    else: pass
    send("{ENTER}{ENTER}%a{ENTER}")
send("{ESC}")
