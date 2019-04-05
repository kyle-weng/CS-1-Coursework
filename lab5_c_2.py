from tkinter import *
import random
import math

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
    global line_list
    for circle in line_list:
        canvas.delete(circle)
    line_list = []

def draw_line(x1, y1, x2, y2):
    global color
    line = canvas.create_line(x1, y1, x2, y2, fill = color)
    return line

def draw_star(x, y):
    '''Creates a colored N-pointed star shape centered at the specified
    coordinates.'''
    global color, line_list, N
    radius = random.randint(50, 100)
    theta_offset = (3 * math.pi / 2)
    for n in range (0, N, 1):
        theta_current = theta_offset + (2 * math.pi / N * n)
        theta_next = theta_offset + (2 * math.pi / N * (n + (N - 1) / 2))
        x1 = x + radius * math.cos(theta_current)
        y1 = y + radius * math.sin(theta_current)
        x2 = x + radius * math.cos(theta_next)
        y2 = y + radius * math.sin(theta_next)
        line_list.append(draw_line(x1, y1, x2, y2))
    
# Event handlers.

def key_handler(event):
    global N
    '''Handle key presses.'''
    if event.keysym == 'q':
        exit()
    elif event.keysym == 'c':
         change_color()
    elif event.keysym == 'x':
        clear_circles()
    elif event.keysym == 'plus':
        N = N + 2
    elif event.keysym == 'minus':
        if N > 5:
            N = N - 2
        

def button_handler(event):
    '''Handle left mouse button click events.'''
    draw_star(event.x, event.y)

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    canvas = Canvas(root, width=800, height=800)
    canvas.pack()
    change_color()
    line_list = []
    N = 5

    # Bind events to handlers.
    root.bind('<Key>', key_handler)
    canvas.bind('<Button-1>', button_handler)      

    # Start it up.
    root.mainloop()

