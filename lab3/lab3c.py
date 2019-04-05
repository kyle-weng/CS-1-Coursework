'''
lab3c.py
Simple L-system simulator.
'''

# References: 
#   http://en.wikipedia.org/wiki/L-systems
#   http://www.kevs3d.co.uk/dev/lsystems/
# N.B. http://en.wikipedia.org/wiki/MU_puzzle for midterm?

import math

# ---------------------------------------------------------------------- 
# Example L-systems.
# ---------------------------------------------------------------------- 

# Koch snowflake.
koch = { 'start' : 'F++F++F', 
         'F'     : 'F-F++F-F' }
koch_draw = { 'F' : 'F 1', 
              '+' : 'R 60', 
              '-' : 'L 60' }

# Hilbert curve.
hilbert  = { 'start' : 'A', 
             'A'     : '-BF+AFA+FB-' , 
             'B'     : '+AF-BFB-FA+' }
hilbert_draw = { 'F' : 'F 1', 
                 '-' : 'L 90', 
                 '+' : 'R 90' }

# Sierpinski triangle.
sierpinski = { 'start' : 'F-G-G', 
               'F'     : 'F-G+F+G-F', 
               'G'     : 'GG' }
sierpinski_draw = { 'F' : 'F 1', 
                    'G' : 'F 1', 
                    '+' : 'L 120', 
                    '-' : 'R 120' }

# ---------------------------------------------------------------------- 
# L-systems functions.
# ---------------------------------------------------------------------- 

def iterate(lsys, n):
    '''Takes an L-system dictionary and and a positive integer n. Returns the string
    after it has been updated n times.'''
    output_string = lsys['start']
    for x in range (0,n):
        output_string = update(lsys, output_string)
    return output_string
    

def lsystemToDrawingCommands(draw, s):
    '''Takes a dictionary with keys that are characters in L-system strings and
    values that are drawing commands and an L-system string. Returns the list of
    drawing commands needed to draw the figure corresponding to the string.'''
    output_list=[]
    for x in range (0,len(s)):
        if s[x] in draw.keys():
            output_list.append(draw[s[x]])
        else:
            output_list.append(s[x])
    return output_list

def bounds(cmds):
    '''Takes a list of commands, computes the bounding coordinates of the resultant
    drawing, and returns a tuple of the minimum x, maximum x, minimum y, and
    maximum y, respectively.'''
    x_min = 0
    x_max = 0
    x_current = 0
    y_min = 0
    y_max = 0
    y_current = 0
    angle_current = 0
    for cmd in cmds:
        (x_current, y_current, angle_current) = nextLocation(x_current, y_current, angle_current, cmd)
        if x_current < x_min:
            x_min = x_current
        elif x_current > x_max:
            x_max = x_current
        if y_current < y_min:
            y_min = y_current
        elif y_current > y_max:
            y_max = y_current
    return (x_min, x_max, y_min, y_max)

def nextLocation(x, y, angle, cmd):
    '''Takes the current x and y coordinate values of the turtle, the current
    angle from the horizontal the turtle is facing, and a drawing command.
    Returns the next location and direction of the turtle after the command has
    been executed as a 3-tuple of x, y, and angle.'''
    split_cmd = cmd.split()
    if split_cmd[0] == 'F':
        x += (math.cos(angle * math.pi / 180.0))
        y += (math.sin(angle * math.pi / 180.0))
    else:
        if split_cmd[0] == 'R':
            angle -= int(split_cmd[1])
        elif split_cmd[0] == 'L':
            angle += int(split_cmd[1])
        
    return (x, y, angle % 360)
    

def saveDrawing(filename, bounds, cmds):
    '''Takes a filename to write the drawing to, the bounds of the drawing (as
    a 4-tuple), and a list of drawing commands. Writes this information to a
    file.'''
    file = open(filename,'w')
    for x in bounds:
        file.write(str(x) + ' ')
    for x in cmds:
        file.write('\n' + str(x))
    file.close()

def makeDrawings(name, lsys, ldraw, imin, imax):
    '''Make a series of L-system drawings.'''
    print('Making drawings for {}...'.format(name))
    for i in range(imin, imax):
        l = iterate(lsys, i)
        cmds = lsystemToDrawingCommands(ldraw, l)
        b = bounds(cmds)
        saveDrawing('%s_%d' % (name, i), b, cmds)

def main():
    makeDrawings('koch', koch, koch_draw, 0, 6)
    makeDrawings('hilbert', hilbert, hilbert_draw, 1, 6)
    makeDrawings('sierpinski', sierpinski, sierpinski_draw, 0, 10)

def update(input_dict, input_string):
    '''Takes a dictionary specifying the starting string and the update rules for
    a particular L-system and an L-system string. Returns the next version of the
    L-system string by applying the L-system rules to each character and combining
    all of the strings. Copies any character not corresponding to a key into the
    new string unchanged.'''
    output_string = ''
    for x in range (0,len(input_string)):
        if input_string[x] in input_dict.keys():
            output_string += input_dict[input_string[x]]
        else:
            output_string += input_string[x]
    return output_string

