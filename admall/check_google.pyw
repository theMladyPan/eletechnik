import ctypes, webbrowser

def getCB():
    ctypes.windll.user32.OpenClipboard(0)
    pcontents = ctypes.windll.user32.GetClipboardData(1)
    data = ctypes.c_char_p(pcontents).value
    ctypes.windll.user32.CloseClipboard()
    return data

webbrowser.open("https://www.google.fr/search?q=%s"%getCB())

