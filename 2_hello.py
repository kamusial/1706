import tkinter as tk

root = tk.Tk()
root.title('Tytul okna - pierwsze okna')
root.geometry('400x300+500+200')
root.iconbitmap('./icon.ico')

message1 = tk.Label(root, text='Siema, pierwszy kod')
message1.pack()
message2 = tk.Label(root, text='Siema, drugi kod')
message2.pack()

root.mainloop()