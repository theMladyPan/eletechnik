from time import sleep
from os import startfile
from SendKeys import SendKeys
startfile("C:\gesco5\\taroffre.exe")
sleep(0.5)
def send(arg):
    SendKeys(arg, turn_off_numlock=False,pause=0.01)

send("{ENTER}")
send("%r")
send("^v")
send("%v")
send("{ENTER}")
send("{ESC}")
