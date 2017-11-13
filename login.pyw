import os, time, urllib
from os.path import expanduser

os.system("C:\gesco5\\logingesco.exe")
time.sleep(1)
os.startfile("C:\gesco5\\accueiltel.exe")
os.startfile("C:\Program Files\\Opera\\launcher.exe")
time.sleep(15)
os.system('REG ADD "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 0 /f')

