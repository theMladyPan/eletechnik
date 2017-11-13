# -*- coding: cp1250 -*-

from time import sleep
import pyexcel, pyexcel_ods, os, ctypes
from SendKeys import SendKeys
from subprocess import call, Popen, PIPE

def sendKey(arg):
    global debug
    if debug: SendKeys(str(arg), turn_off_numlock=False,pause=0.3)
    else: SendKeys(str(arg), turn_off_numlock=False,pause=0.03)

def setCB(text):
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
    sleep(0.01)

def insert(ref, moq, desig, minif, info, tarif, purchase, special):
    print "Upravujem: ",ref, moq, desig, minif, info, tarif, purchase, special
    sendKey("%rm")
    try: setCB(ref.replace(".0",""))
    except: setCB(ref)
    sendKey("^v") 
    sendKey("~"*3)
    if moq:
        setCB("%d"%int(moq))
        sendKey("^v")
    sendKey("~")
    if desig:
        setCB(desig)
        sendKey("^v")   
    sendKey("{TAB}")
    if minif:
        setCB("%d"%int(minif))
        sendKey("^v")
    
    sendKey("{TAB}"*2)
    if info:
        setCB(info)
        sendKey("^v") 
    sendKey("~"*3)  
    if tarif:
        setCB("%.2f"%tarif)
        sendKey("^v")
    sendKey("~"*2)
    
    if purchase:
        setCB("%.2f"%purchase)
        sendKey("^v")
        
    sendKey("~")
    sendKey("+{TAB}")
    
    if special:
        setCB("%.2f"%special)
        sendKey("^v") 
        
    sendKey("{TAB}")
    sendKey("~"*5)  
    sendKey("%a")

if __name__ == "__main__":
    debug=input("Debug mode (0-no, 1-yes) - ")
    os.system("C:\gesco5\\taroffre.exe")
    
    sheet=pyexcel.load("items.ods")
    data = sheet.row[1:]

    for riadok in data:
        if riadok[0]!= "": insert(riadok[0],riadok[1],riadok[2],riadok[3],riadok[4],riadok[5], riadok[6], riadok[7])
    
