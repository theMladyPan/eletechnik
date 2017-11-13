import ctypes, time
from SendKeys import SendKeys

debug=input("debug? 1/0:")
def send(arg):
    SendKeys(arg, turn_off_numlock=False,pause=0.01+debug*0.1)
    
i=0
dokedy=input("kolko krat? ")
time.sleep(3)

while i<dokedy:
    ctypes.windll.user32.SetCursorPos(700,550)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up
    time.sleep(0.1)
    send("{UP}")
        
    ctypes.windll.user32.SetCursorPos(550,630)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up
    time.sleep(0.01)
    send("{UP}"*3)
    send("{DOWN}")
    time.sleep(0.01)
    i+=1
