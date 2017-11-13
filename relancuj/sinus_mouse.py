import ctypes, time, math

while 1:
    x=int(time.time()*300%1920)
    ctypes.windll.user32.SetCursorPos(x,int(math.sin(x/300.0)*540)+540)
    time.sleep(0.001)
