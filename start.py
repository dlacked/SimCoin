from tkinter import *
import tkinter.ttk
import time

root = Tk()
root.title("SimCoin")
root.geometry("600x1000+700+35")
root.resizable(0, 0)

image=tkinter.PhotoImage(file="image\image\start.png")

label=tkinter.Label(root, image=image)
label.pack()
root.mainloop()

os.system("taskkill /f /im start.exe")
