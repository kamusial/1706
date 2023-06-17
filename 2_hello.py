import tkinter as tk

root = tk.Tk()
root.title('Tytul okna - pierwsze okna')
root.geometry('400x300+500+200')
root.iconbitmap('./icon.ico')
#root.resizable(True, False)    $zablokowanie możliowści zmiany okna
root.minsize(200, 200)
root.maxsize(800, 600)
root.attributes('-topmost', 1)   # zawsze na wierzchu
root.attributes('-alpha', 0.9)   #przezroczystosc
root.config(background='Light Blue')  #   #ccc albo #555

message1 = tk.Label(root, text='Siema, pierwszy kod')
message1.pack(ipadx=55, ipady=10, padx=5, pady=5)
message2 = tk.Label(root, text='Siema, drugi kod')
message2.pack(ipadx=55, ipady=10)

exit_button = tk.Button(root, text='Wyjscie', command=lambda: root.quit())
exit_button.pack(ipadx=55, ipady=10, expand=True)    #dodatkowe miejsce

root.mainloop()