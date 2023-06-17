from tkinter import *

root = Tk()
root.geometry('750x400')

def callback(e):
    print(e)
    print(e.x, e.y)

root.bind('<Motion>',callback)
root.mainloop()