import random

def random_size(int1, int2):
    '''Takes two non-negative even integers such that int2 < int1. Returns a
    random even integer that is >= int2 and <= int1.'''
    assert ((int1 >= 0) and (int2 >= 0))
    assert ((int1 % 2 == 0) and (int2 % 2 == 0))
    assert (int1 < int2)
    output = 2 * random.randint(int1 / 2, int2 / 2)
    assert (output % 2 == 0)
    return output

def random_position(max_x, max_y):
    '''Takes two positive integers and returns a random (x, y) tuple with x and
    y positive and less than or equal to their respective maximums.'''
    return (random.randint(0, max_x), random.randint(0, max_y))

def random_color():
    '''Generates random color values in a format recognizable by tkinter. The 
    strings are of form #RRGGBB, where # is the literal character '#' and 
    'RRGGBB' are six hexadecimal digits; 'RR' represents the degree of red color,
    'GG' represents the degree of green color, and 'BB' represents the degree of
    blue color. The minimum value for each color is 00 and the maximum is ff.'''
    return_string = "#"
    while (len(return_string) < 7):
        return_string += hex(random.randint(0,15))[2:]
    return return_string

def count_values(input_dict):
    '''Takes a single dictionary as an argument and returns a count of the
    number of distinct values it contains.'''
    n = 0
    counted_list = []
    for x in list(input_dict.values()):
        if x in counted_list:
            continue
        else:
            n += 1
            counted_list.append(x)
    return n

def remove_value(input_dict, object_to_remove):
    '''Takes an input dictionary and an item to remove from that dictionary (if
    it exists in it). It removes all key/value pairs from the dictionary with
    that value. If the value is not in the dictionary, it does nothing. It
    returns nothing.'''
    keys = []
    for x in range(0,len(list(input_dict.values()))):
        if object_to_remove == list(input_dict.values())[x] :
            keys.append(list(input_dict.keys())[x])
    for x in keys:
        del input_dict[x]

def split_dict(input_dict):
    '''Takes as an argument a dictionary which uses strings as keys and returns
    a tuple of two dictionaries who key/value pairs are from the original
    dictionary. One dictionary has keys starting with the letters a-m; the other
    has keys starting with the letters n-z.'''
    a_to_m = {}
    n_to_z = {}
    for x in list(input_dict.keys()):
        if x[:1].lower() <= 'm':
            a_to_m[x] = input_dict[x]
        elif x[:1].lower() >= 'n':
            n_to_z[x] = input_dict[x]
    return (a_to_m, n_to_z)

def count_duplicates(input_dict):
    '''Takes an dictionary and returns the number of values that appear two or
    more times.'''
    n = 0
    counted_values = []
    for x in list(input_dict.values()):
        if (list(input_dict.values()).count(x) > 1) and (x not in counted_values):
            n += 1
            counted_values.append(x)
    return n