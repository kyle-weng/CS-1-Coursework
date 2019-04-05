from tkinter import *
import random

# Graphics commands.


# Event handlers.

def key_handler(event):
    '''Handle key presses.'''
    pass

def button_handler(event):
    '''Handle left mouse button click events.'''
    pass

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    canvas = Canvas(root, width=800, height=800)
    canvas.pack()

    # Bind events to handlers.
    root.bind('<Key>', key_handler)
    canvas.bind('<Button-1>', button_handler)
    

    # Start it up.
    root.mainloop()

