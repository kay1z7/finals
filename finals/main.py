from msilib.schema import Icon
from tkinter import *

class Window:
    def __init__ (self, width, height, resizable=(False, False), icon=None ):
        self.root = Tk()
        self.geometry(f"{width}x{height}+200+200")
        self.root.resizable(resizable[0], resizable[1])
        if Icon:
            self.root.iconbitmap(Icon)

    def run(self):
        self.root.mainloop()   

'''window = Tk()
window.geometry("400x500+600+300")
window.resizable(False, False)
window.iconbitmap("logo.ico")

window.mainloop()
'''