'''
This module simulates balls bouncing around a canvas.
'''

import math, random, time
from tkinter import *

class BouncingBall:
    '''Objects of this class represent balls which bounce on a canvas.'''

    def __init__(self, canvas, center, radius, color, direction, speed):
        '''
        Create a new ball with a given location, direction, color, and speed.

        Arguments:
          canvas:    the canvas the ball moves on
          center:    the center of the ball in (x, y) pixel coordinates
          radius:    the radius of the ball in pixels
          color:     the color of the ball
          direction: the initial direction the ball is moving
          speed:     the initial speed of the ball
        '''

        x, y = center
        x1 = x - radius
        y1 = y - radius
        x2 = x + radius
        y2 = y + radius
        self.handle = canvas.create_oval(x1, y1, x2, y2,
                        fill=color, outline=color)
        self.canvas = canvas
        self.xmax   = int(canvas.cget('width')) - 1
        self.ymax   = int(canvas.cget('height')) - 1
        self.center = center
        self.radius = radius
        self.color  = color

        # The direction is represented as an angle in degrees
        # (range 0-360), which we convert to radians here.
        # The angle is with respect to the positive x axis,
        # going clockwise around the origin.
        if direction < 0.0 or direction > 360.0:
            raise ValueError('Invalid direction; must be in range [0.0, 360.0]')
        dir_radians = direction * math.pi / 180.0

        # Separate the direction into its x and y coordinates.
        # Flip the sign of the y coordinate because the y coordinate
        # grows downward, not upward.
        self.dirx = math.cos(dir_radians)
        self.diry = -math.sin(dir_radians)

        # Speed is represented as a single non-negative float.
        # Note that non-float speeds will behave poorly.
        if speed < 0.0: 
            raise ValueError('Invalid speed; must be positive')
        self.speed = speed

    def step(self):
        '''
        Move this ball in its current direction with its current speed.  
        Change direction if the edge of the canvas is reached.

        Arguments: none
        Return value: none
        '''
        
        vx = self.speed * self.dirx
        vy = self.speed * self.diry
        
        disp_x = self.displacement(self.center[0], vx, self.xmax)
        disp_y = self.displacement(self.center[1], vy, self.ymax)
        
        if disp_x != vx:
            self.dirx = -self.dirx
        if disp_y != vy:
            self.diry = -self.diry
        
        self.center = (self.center[0] + disp_x, self.center[1] + disp_y)
        self.canvas.move(self.handle, disp_x, disp_y)

    def displacement(self, c, d, cmax):
        '''
        Compute the actual displacement along the x or y dimension,
        taking reflections off the edge into account.  
        
        Arguments:
          c:    the center of the ball (x or y coordinate)
          cmax: the largest value in that direction
          d:    the desired displacement in that direction

        Return value: the computed displacement
        '''
        if c + d > cmax - self.radius:
            delta = 2 * (cmax - self.radius) - 2 * c - d
        elif c + d < self.radius:
            delta = d - c + self.radius
        else:
            delta = d
        return delta

    def scale_speed(self, scale):
        '''
        Scale the speed of this object.
        
        Arguments: 
          scale: the speed scaling factor

        Return value: none
        '''

        self.speed *= scale

    def delete(self):
        '''
        Remove this object from the canvas.

        Arguments: none
        Return value: none
        '''

        self.canvas.delete(self.handle)



def random_ball(canvas, rmin, rmax, smin, smax, xmax, ymax):
    '''
    Create and return a ball with a random color, starting position,
    size, direction, and velocity.
    rmin: minimum radius (pixels)
    rmax: maximum radius (pixels)
    smin: minimum speed
    smax: maximum speed
    xmax: maximum x dimension of canvas
    ymax: maximum y dimension of canvas
    '''
    
    def generate_color():
        '''Randomly generates a color.'''
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        r_hex = hex(r)[2:]
        g_hex = hex(g)[2:]
        b_hex = hex(b)[2:]
        if len(r_hex) < 2:
            r_hex = "0" + r_hex
        if len(g_hex) < 2:
            g_hex = "0" + g_hex
        if len(b_hex) < 2:
            b_hex = "0" + b_hex
        rgb_hex = "#" + r_hex + g_hex + b_hex
        return rgb_hex
    
    radius = random.randint(rmin, rmax)
    speed = random.randint(smin, smax)
    color = generate_color()
    direction = random.random() * 360
    cx = random.randint(radius, xmax - radius)
    cy = random.randint(radius, ymax - radius)
    
    return BouncingBall(canvas, (cx, cy), radius, color, direction, speed)

def key_handler(event):
    '''Handle key presses.'''
    global bouncing_balls
    global done
    key = event.keysym
    if key == 'q': 
        done = True
        exit()
    elif key == 'plus':  # add a ball at a random location
        ball = random_ball(canvas, 10, 60, 5.0, 15.0, 800, 600)
        bouncing_balls.append(ball)
    elif key == 'minus':  # remove a ball from the canvas if there are any
        if len(bouncing_balls) > 0:
            index_to_remove = random.randint(0, len(bouncing_balls) - 1)
            ball_to_remove = bouncing_balls[index_to_remove]
            ball_to_remove.delete()
            bouncing_balls.remove(ball_to_remove)
    elif key == 'u':  # speed (u)p all bouncing_balls by factor of 1.2
        for ball in bouncing_balls:
            ball.scale_speed(1.2)
    elif key == 'd':  # slow (d)own all bouncing_balls by factor of 1.2
        for ball in bouncing_balls:
            ball.scale_speed(1 / 1.2)
    elif key == 'x':  # delete all bouncing_balls
        for ball in bouncing_balls:
            ball.delete()
        bouncing_balls = []

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x600')
    canvas = Canvas(root, width=800, height=600)
    canvas.pack()
    done = False

    # Bind events to handlers.
    root.bind('<Key>', key_handler)
    
    # Set up some bouncing balls.
    bouncing_balls = []
    for i in range(5):
        bouncing_balls.append(random_ball(canvas, 10, 60, 5.0, 15.0, 800, 600))

    # Start the event loop.
    while not done:
        time.sleep(0.001)  # add a slight delay to smooth out the simulation
        for ball in bouncing_balls:
            ball.step()
        root.update()

