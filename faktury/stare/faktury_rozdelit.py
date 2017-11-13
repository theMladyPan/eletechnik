# -*- coding: utf-8 -*-
from time import sleep
try:
    with file("original.pdf","r") as subor:
        data=subor.read()
    with file("klienti.txt","r") as subor:
        klienti=subor.read().split("\n")
        print "Separujem faktury pre:\n"
        for i in klienti:
            print i
        
except:
    raw_input("V priecinku sa nenachadza subor original.pdf alebo klienti.txt. Koncim.")
    sleep(2)
    exit(0)



faktury=data.split("stream")
for klient in klienti:
    zoznam_faktur=""
    obj=2
    stran=0
    
    for faktura in faktury:
        if klient in faktura:
            stran+=1
            obj+=2
            zoznam_faktur+= "%d 0 obj\n<<\n/Type /Page\n/Parent 3 0 R\n/Contents %d 0 R\n/MediaBox [0 0 595 841]\n>>\nendobj\n%d 0 obj\n<< /Length 17985 >>\nstream\n%s\nendstream\nendobj\n"%(obj,obj+1, obj+1,faktura[:-3]) 

    with file("upravene\\"+klient+".pdf", "w") as subor:
        subor.write("""
%PDF-1.3
%Å­o
1 0 obj
<<
/Type /Catalog
/Pages 3 0 R
/Outlines 2 0 R
/ViewerPreferences << /HideToolbar false /FitWindow true >>
>>
endobj
2 0 obj
<<
/Type /Outlines
/Count 0
>>
endobj
3 0 obj
<<
/Type /Pages""")
        subor.write("""
/Count %d
/Kids [4 0 R 6 0 R 8 0 R 10 0 R 12 0 R 14 0 R 16 0 R 18 0 R 20 0 R 22 0 R 24 0 R 26 0 R 28 0 R 30 0 R 32 0 R 34 0 R 36 0 R 38 0 R 40 0 R 42 0 R 44 0 R 46 0 R 48 0 R 50 0 R 52 0 R 54 0 R 56 0 R 58 0 R 60 0 R 62 0 R 64 0 R 66 0 R 68 0 R 70 0 R 72 0 R 74 0 R 76 0 R 78 0 R 80 0 R 82 0 R 84 0 R 86 0 R 88 0 R 90 0 R 92 0 R 94 0 R 96 0 R 98 0 R 100 0 R 102 0 R 104 0 R 106 0 R 108 0 R 110 0 R 112 0 R 114 0 R 116 0 R 118 0 R 120 0 R 122 0 R 124 0 R 126 0 R 128 0 R 130 0 R 132 0 R 134 0 R 136 0 R 138 0 R 140 0 R 142 0 R 144 0 R 146 0 R 148 0 R 150 0 R 152 0 R 154 0 R 156 0 R 158 0 R 160 0 R 162 0 R 164 0 R 166 0 R 168 0 R 170 0 R 172 0 R 174 0 R 176 0 R 178 0 R 180 0 R 182 0 R 184 0 R 186 0 R 188 0 R 190 0 R 192 0 R 194 0 R 196 0 R 198 0 R 200 0 R 202 0 R 204 0 R 206 0 R 208 0 R 210 0 R 212 0 R 214 0 R 216 0 R 218 0 R 220 0 R 222 0 R 224 0 R 226 0 R 228 0 R 230 0 R 232 0 R 234 0 R 236 0 R 238 0 R]
/MediaBox [0 0 595 841]
/Resources << 
/Font << 
  /F00 240 0 R 
  /F01 242 0 R 
  /F02 244 0 R 
  /F03 246 0 R 
  /F04 248 0 R 
  /F05 250 0 R 
  >>
/ProcSet 253 0 R
>>
>>
endobj
%s
%s
"""%(stran, zoznam_faktur, faktury[-1]))
sleep(2)
