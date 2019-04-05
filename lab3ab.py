#Ex. A.1:
def list_reverse(input_list):
    '''Takes an input list and returns its reverse without changing
    the original input.'''
    output_list = input_list.copy()
    output_list.reverse()
    return output_list

#Ex. A.2:
def list_reverse2(input_list):
    '''Takes an input list and returns its reverse without changing
    the original input.'''
    output_list = []
    for i in range(len(input_list)-1,-1,-1):
        output_list.append(input_list[i])
    return output_list

#Ex. A.3:
def file_info(path):
    '''Takes a string representing the path (or the name) of a text file.
    Returns the number of lines, the number of words, and the number of
    characters in the file as a three-part tuple.'''
    file = open(path, 'r')
    number_of_lines = 0
    number_of_words = 0
    number_of_chars = 0
    for line in file:
        number_of_lines += 1
        number_of_words += len(line.split())
        chars_in_line = 0
        for char in line:
            if char != ' ':
                chars_in_line += 1
        number_of_chars += chars_in_line
    file.close()
    return (number_of_lines, number_of_words, number_of_chars)

#Ex. A.4:
def file_info2(path):
    '''Takes a string representing the path (or the name) of a text file.
    Returns the number of lines, the number of words, and the number of
    characters in the file as a dictionary.'''
    input_tuple = file_info(path)
    return {'lines': input_tuple[0],
            'words': input_tuple[1],
            'characters': input_tuple[2]}
    
#Ex. A.5:
def longest_line(path):
    '''Takes a string representing the path (or the name) of a text file.
    Returns the length of the longest line in the file, as well of the line itself,
    as a tuple. If multiple lines tie for the longest line, return the information
    corresponding to the first such line.'''
    file = open(path, 'r')
    length = 0
    for line in file:
        chars_in_line = 0
        for char in line:
            if char != ' ':
                chars_in_line += 1
        length_old = length
        length = max(length,chars_in_line)
        if length != length_old:
            text = line
    return (length,text)

#Ex. A.6:
def sort_words(input_string):
    '''Takes a string, splits it into a list of words, sorts the list, and returns
    the sorted list.'''
    split_list = input_string.split()
    split_list.sort()
    return(split_list)
    
#Ex. A.7: convert 11011010 from binary to decimal
# 1 * 2^7 + 1 * 2^6 + 0 * 2^5 + 1 * 2^4 + 1 * 2^3 + 0 * 2^2 + 1 * 2^1 + 0 * 2^0 = 218
# The largest 8 digit binary number is 11111111. Its decimal expansion is
# 2^7 + 2^6 + 2^5 + 2^4 + 2^3 + 2^2 + 2^1 + 2^0 = 255

#Ex. A.8:
def binaryToDecimal(input_list):
    '''Takes a list of zeroes and ones, ordered such that the list corresponds
    to a binary number. Returns the decimal integer equivalent.'''
    dec = 0
    for i in range(0,len(input_list)):
        dec += input_list[i] * (2 ** (len(input_list)-1-i))
    return dec

#Ex. A.9:
def decimalToBinary(input_int):
    '''Takes a decimal integer and converts it to a list of zeroes and ones, 
    ordered such that the list corresponds to a binary number. Returns that list.'''
    
    def findGreatestPowerOfTwoDivisor(input_int):
        '''Takes an input integer and finds a divisor such that it is large as
        possible and that it is a power of two. Returns the power.'''
        power = 0
        while(input_int % (2**(power+1)) != input_int):
            power += 1
        return power
    
    place_value = findGreatestPowerOfTwoDivisor(input_int) + 1
    remainder = input_int
    output_list = []
    while((remainder > 0) or (place_value > 0)):
        old_remainder = remainder
        place_value -= 1
        remainder %= (2**place_value)
        if (remainder != old_remainder):
            output_list.append(1)
        else:
            output_list.append(0)
    return output_list

#Ex. B.2.1:
# 1. There is no space after each comma in the signature.
# 2. No parentheses are used to show operator precedence.
# 3. There are no spaces between the variables and operators.
# 4. The name of the function is nondescriptive.
def sum_of_cubes(a, b, c):
    return (a * a * a) + (b * b * b) + (c * c * c)

#Ex. B.2.2:
# 1. There is a spelling error in the comment.
# 2. No parentheses are used to show operator precedence.
# 3. There are no spaces between the variables and operators.
# 4. The names of the parameters are redundant (it is already obvious that they
#    are arguments.)
# 5. Partially because the variables/functions are named so awkwardly, it is
#    difficult to distinguish between multiple words in the same variable name.
def sumOfCubes(a, b, c, d):
    # Return sum of cubes of a, b, c, and d
    return (a ** 3) + (b ** 3) + (c ** 3) + (d ** 3)

#Ex. B.2.3:
# 1. The indentation is inconsistent.
# 2. There is a blank line missing between the end of one function and the 
#    beginning of the next.
def sum_of_squares(x, y):
    return (x * x) + (y * y)

def sum_of_three_cubes(x, y, z):
    return (x * x * x) + (y * y * y) + (z * z * z)



        