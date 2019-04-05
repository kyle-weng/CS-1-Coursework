from tkinter import *

root = Tk()
root.geometry('800x800')
c = Canvas(root, width=800, height=800)
c.pack()
red = c.create_rectangle(0, 0, 100, 100, fill='red', outline='red')
blue = c.create_rectangle(100, 700, 0, 800, fill='blue', outline='blue')
green = c.create_rectangle(700, 100, 800, 0, fill='green', outline='green')
yellow = c.create_rectangle(700, 700, 800, 800, fill='yellow', outline='yellow')
root.mainloop()