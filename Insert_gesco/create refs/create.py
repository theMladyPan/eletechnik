# -*- coding: cp1250 -*-

from time import sleep
import pyexcel, pyexcel_ods
from SendKeys import SendKeys
import platform, os, ctypes, webbrowser, tempfile
from subprocess import call, Popen, PIPE

debug=input("Debug mode (0-no, 1-yes) - ")

def sendKey(arg):
    global debug
    if debug: SendKeys(str(arg), turn_off_numlock=False,pause=0.2)
    else: SendKeys(str(arg), turn_off_numlock=False,pause=0.02)

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

def insert(marque, ref, moq, desig, minif, info, tarif, purchase):
    print marque, ref, moq, desig, minif, info, tarif, purchase
    sendKey("%rc")
    setCB(marque)
    sendKey("^v") 
    sendKey("{TAB}")
    sendKey("{ESC}")
    setCB(ref.replace(".0",""))
    sendKey("^v")    
    sendKey("{TAB}")
    sendKey("%d"%int(moq))
    sendKey("{TAB}") 
    setCB(desig)
    sendKey("^v") 
    sendKey("{TAB}")
    sendKey("%d"%int(minif))
    sendKey("{TAB}"*2)
    setCB(info)
    sendKey("^v")
    sendKey("{TAB}"*2)    
    sendKey("%s"%tarif)
    sendKey("{TAB}"*2)
    sendKey("%s"%purchase)
    sendKey("~"*7)
    sendKey("a")

if __name__ == "__main__":

    sleep(1)
    sheet=pyexcel.load("items.ods")
    data = sheet.row[1:]
    print "marque, ref, moq, desig, minif, info, tarif, purchase"
    for riadok in data:
        if riadok[0]!= "": insert(riadok[0],riadok[1],riadok[2],riadok[3],riadok[4],riadok[5],riadok[6], riadok[7])
    
