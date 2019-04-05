from tkinter import *

def draw_square(canvas, color, side_length, center):
    '''Takes the canvas on which the square will the drawn, the color of the
    square, the side length of the square, and the position of the center of
    the square, represented as a tuple of two integers representing the horizontal
    and vertical position of the center in pixels. Draws the corresponding square
    on the corresponding canvas, and returns the square's handle.'''
    sq = canvas.create_rectangle(center[0] - (side_length / 2), center[1] -
        (side_length / 2), center[0] + (side_length / 2), center[1] +
        (side_length / 2), fill = color, outline = color)
    return sq

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    c = Canvas(root, width=800, height=800)
    c.pack()
    blue = draw_square(c, 'blue', 100, (50, 750))
    yellow = draw_square(c, 'yellow', 100, (750, 750))
    red = draw_square(c, 'red', 100, (50, 50))
    green = draw_square(c, 'green', 100, (750, 50))
    root.mainloop()