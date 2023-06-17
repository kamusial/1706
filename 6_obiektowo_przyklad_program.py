import tkinter as tk

class MyGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Moje gui')
        self.root.geometry('600x400+50+20')
        self.root.attributes('-alpha', 0.9)
        self.root.config(background='#c51')
        self.root.attributes('-topmost', 1)

        self.label = tk.Label(self.root, text='moj text..........')
        self.label.config(
            background='#555',
            fg='#cc1',
            font=('Arial', 23),
            padx=20,
            pady=5)
#        self.label.pack()
#        self.label.place(x=30, y=40, height=100, width=120)
        self.label.grid(row=0, column=0, rowspan=2, columnspan=2)

        self.label2 = tk.Label(self.root, text='moj text2')
        self.label2.config(
            background="#555",
            fg="#ccc",
            font=("Arial", 20),
            padx=20,
            pady=10)
        self.label2.grid(row=3, column=3)

        self.root.mainloop()

MyGUI()