from Tkinter import Tk
from ttk import Label, Button
class dialog:
    def __init__(self, titulok="Pozor", sprava="Pozor"):
        self.main=Tk()
        self.main.title(titulok)
        Label(self.main, text=sprava).pack()
        Button(self.main, text="Ok", command=self.main.destroy).pack()
        self.main.mainloop()

if __name__ == "__main__":
    dialog(sprava="prazdny dialog")
