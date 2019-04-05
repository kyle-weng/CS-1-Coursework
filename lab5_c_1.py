from tkinter import *
import random

# Graphics commands.

def change_color():
    global color
    '''Randomly changes the current color.'''
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r_hex = hex(r)[2:]
    g_hex = hex(g)[2:]
    b_hex = hex(b)[2:]
    rgb_lst = [r_hex, g_hex, b_hex]
    if len(r_hex) < 2:
        r_hex = "0" + r_hex
    if len(g_hex) < 2:
        g_hex = "0" + g_hex
    if len(b_hex) < 2:
        b_hex = "0" + b_hex
    rgb_hex = "#" + r_hex + g_hex + b_hex
    color = rgb_hex

def clear_circles():
    '''Clears all circles from the canvas.'''
    global circle_list
    for circle in circle_list:
        canvas.delete(circle)
    circle_list = []

def create_circle(x, y):
    '''Creates a circle of the current color and a random diameter between 10
    and 50 pixels that is centered at the current position of the mouse
    cursor.'''
    global color, circle_list
    diameter = random.randint(10, 50)
    circle = canvas.create_oval(x - diameter / 2, y - diameter / 2, 
                                x + diameter / 2, y + diameter / 2,
                                fill = color, outline = color)
    circle_list.append(circle)
    

# Event handlers.

def key_handler(event):
    '''Handle key presses.'''
    if event.keysym == 'q':
        exit()
    elif event.keysym == 'c':
         change_color()
    elif event.keysym == 'x':
        clear_circles()

def button_handler(event):
    '''Handle left mouse button click events.'''
    create_circle(event.x, event.y)

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    canvas = Canvas(root, width=800, height=800)
    canvas.pack()
    change_color()
    circle_list = []

    # Bind events to handlers.
    root.bind('<Key>', key_handler)
    canvas.bind('<Button-1>', button_handler)    

    # Start it up.
    root.mainloop()

