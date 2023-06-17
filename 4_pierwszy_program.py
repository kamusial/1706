import tkinter as tk
root = tk.Tk()

root.geometry('500x600')
root.title('program z przyciskami')

label = tk.Label(root, text='Hello', font=('Arial', 28))
label.pack(padx=10, pady=20)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=2)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text='1', font=('Arial', 15))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
btn2 = tk.Button(buttonframe, text='2', font=('Arial', 15))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)
btn3 = tk.Button(buttonframe, text='3', font=('Arial', 15))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)
btn4 = tk.Button(buttonframe, text='4', font=('Arial', 15))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)
btn5 = tk.Button(buttonframe, text='5', font=('Arial', 15))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)
btn6 = tk.Button(buttonframe, text='6', font=('Arial', 15))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)
buttonframe.pack(fill='x')

next_button = tk.Button(root, text='Testowy')
next_button.place(x=200, y=100, height=100, width=100)

root.mainloop()