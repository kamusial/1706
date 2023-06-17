import tkinter as tk

class MyGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Moje gui')
        self.root.geometry('600x400+50+20')
        self.root.attributes('-alpha', 0.9)
        self.root.config(background='#c51')
        self.root.attributes('-topmost', 1)



        #Labelka
        self.label = tk.Label(self.root, text='wpisz cos:', font=('Arial', 22))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=3, font=('Arial', 18))
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text='zaznacz', font=('Arial', 14), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text='nacisnij', font=('Arial', 16))
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()


MyGUI()


