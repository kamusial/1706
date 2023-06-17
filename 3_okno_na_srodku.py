import tkinter as tk
root = tk.Tk()
root.title('Wyśrodkowane')
window_width = 500
window_height = 400
screen_width = root.winfo_screenwidth()    # pobranie rozmiaru ekranu
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.mainloop()
