import pyperclip
from time import sleep

old=""

while True:
    try:
        if pyperclip.paste() != old:
            print pyperclip.paste(),"\b"
            pyperclip.copy(pyperclip.paste().replace(" ","").replace("-","").replace("_","").replace("\n","").replace("\r","").replace("	"," "))
            
            old=pyperclip.paste()
        else:
            pass
    except:
        pass
    sleep(0.1)
    
