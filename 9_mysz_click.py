from tkinter import *

def pojedyncze(event):
    print('pojedyncze nacisniecie')

def podwojne(event):
    print('podwojne nacisniecie')

def wyjscie(event):
    import sys; sys.exit()

widget = Button(None, text='klikanie mysza')
widget.pack()
widget.bind('<Button-1>', pojedyncze)
widget.bind('<Double-1>', wyjscie)



widget.mainloop()