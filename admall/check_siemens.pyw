from time import sleep
import platform, os, ctypes, webbrowser, tempfile
from subprocess import call, Popen, PIPE

def getCB():
    ctypes.windll.user32.OpenClipboard(0)
    pcontents = ctypes.windll.user32.GetClipboardData(1)
    data = ctypes.c_char_p(pcontents).value
    ctypes.windll.user32.CloseClipboard()
    return data

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

header="""<html>
  <body style="display:none;">
    <div>
      <form name="SUBMITFORM" method="post" ENCTYPE="MULTIPART/FORM-DATA" action="https://mall.industry.siemens.com/goos/catalog/Pages/ca01/intreceivepartslist.ashx" target="_top">
        <span style="width:1;height:1" />
        <textarea name="xmlpayload" cols="100" rows="50">
          <cart IF_VERSION="2.0">
"""
footer="""
          </cart>
        </textarea>
        <input type="submit" value="go" />
      </form>
      <script language="JavaScript">document.SUBMITFORM.submit();</script>
    </div>
  </body>
</html>"""

body=""

siemens=True
if type(getCB()) == type("a") and ("\r\n" not in getCB() or len(getCB().split("\r\n")[1])==0):
    i=getCB().replace(" ","")
    with open("\\\\servag60\\UTILISATEURS\\fichierscommun\\!!!SOFT\\python\\admall\\refs.db", "r") as subor:
        data=subor.read().split("\n")
    for riadok in data:
        if i[0:3].upper()==riadok[0:3]:
            #print len(riadok[4:].replace("%s",i[3:]))
            webbrowser.open(riadok.split(" ")[1].replace("%s",i.replace("-","").replace(riadok.split(" ")[0],"")))
            siemens=False
   
    if siemens:
        i=getCB().replace(" ","").replace("-","").replace("\n","").replace("\r","")
        setCB(i)
        webbrowser.open("https://mall.industry.siemens.com/mall/en/sk/Catalog/Product/%s"%i)
        #webbrowser.open("https://mall.industry.siemens.com/tedservices/DatasheetService/DatasheetService?control=%3C%3Fxml+version%3D%221.0%22+encoding%3D%22UTF-8%22%3F%3E%3Cpdf_generator_control%3E%3Cmode%3EPDF%3C%2Fmode%3E%3Cpdmsystem%3EPMD%3C%2Fpdmsystem%3E%3Ctemplate_selection+mlfb%3D%22"+i+"%22+system%3D%22PRODIS%22%2F%3E%3Clanguage%3Een%3C%2Flanguage%3E%3Ccaller%3EMall%3C%2Fcaller%3E%3C%2Fpdf_generator_control%3E")
else:
    for i in getCB().split("\r\n"):
        i=i.split(chr(9))
        if i[0]=="":continue
        try:
            if len(i)>1:
                body='            <item PRODUCT_ID="%s" QUANTITY="%d" />\n'%(i[1],int(i[0]))+body
            else:
                body='            <item PRODUCT_ID="%s" QUANTITY="1" />\n'%(i[0])+body
        except ValueError:
            pass

    with tempfile.NamedTemporaryFile("w", suffix=".html") as subor:
        subor.write(header+body+footer)
        subor.flush()
        webbrowser.open(subor.name)
        sleep(5)
