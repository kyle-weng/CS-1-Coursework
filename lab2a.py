#This is a note to myself:
#Make sure you write a docstring for every function we ask you to write.
#It should describe what the function does, what the arguments represent, and what the return value represents.
import random

#Ex. B.1:
def complement(input_string):
    '''Takes a string composed of the letters \'A\', \'C\', \'G\', and \'T\'.
    Returns another string of the same length that represents the DNA complement of
    the input string.'''
    
    def replace(input_char):
        '''Takes an input character and returns its DNA complement.'''
        return {'A': 'T',
                'T': 'A',
                'G': 'C',
                'C': 'G',}[input_char]
    
    output_string = ''
    for input_char in input_string:
        output_string += replace(input_char)
    return output_string

#Ex. B.2:
def list_complement(input_list):
    '''Takes a list with elements \'A\', \'C\', \'G\', and \'T\'.
    Changes the list to one that represents the DNA complement of
    the input list.'''
    
    def replace(input_char):
        '''Takes an input character and returns its DNA complement.'''
        return {'A': 'T',
                'T': 'A',
                'G': 'C',
                'C': 'G',}[input_char]

    for x in range(len(input_list)):
        input_list[x] = replace(input_list[x])

#Ex. B.3:
def product(input_list):
    '''Takes an input list of numbers. Returns the product of the numbers.
    If the input is an empty list, returns 1.'''
    if len(input_list) == 0:
        return 1
    product = 1
    for element in input_list:
        product *= element
    return product

#Ex. B.4:
def factorial(input_int):
    '''Takes an integer. Returns that integer's factorial.'''
    return product(range(1,input_int+1))

#Ex. B.5:
def dice(m,n):
    '''Takes m, which is the number of sides of a hypothetical dice, and n, which
    is the number of times said dice is rolled. Returns the sum of the values rolled.'''
    total = 0
    for i in range(1,n+1):
        total += random.choice(range(1,m+1))
    return total

#Ex. B.6:
def remove_all(input_list, input_value):
    '''Takes an input list and a value to remove all copies of from the list.
    It does not return anything but rather changes the input list.'''
    number_of_occurrences = input_list.count(input_value)
    while number_of_occurrences > 0:
        input_list.remove(input_value)
        number_of_occurrences -= 1

#Ex. B.7:
def remove_all2(input_list,input_value):
    '''Takes an input list and a value to remove all copies of from the list.
    It does not return anything but rather changes the input list.'''
    input_list_clone = list.copy(input_list)
    for x in input_list_clone:
        if x == input_value:
            input_list.remove(input_value)
def remove_all3(input_list,input_value):
    '''Takes an input list and a value to remove all copies of from the list.
    It does not return anything but rather changes the input list.'''
    while input_value in input_list:
        input_list.remove(input_value)

#Ex. B.8:
def any_in(lst1, lst2):
    '''Returns True if any element in list lst1 is equal to any element in list lst2.'''
    return bool(set(lst1).intersection(set(lst2)))

#NOTE FOR SECTION C: The directions were rather vague, so I corrected the code for every question here
    # whenever a corrected version of the code was not also present.

#Ex. C.1.a: The single equals sign should be a double equals sign to check for equality.
    #The single equals sign is used to initialize variables, not check for equality.
#a = 20
# ... later in the program, test to see if a has become 0.
#if a == 0:
#    print('a is zero!')
    

#Ex. C.1.b: 's' in the function's signature should be changed to s because the function
    # is asking for an input variable.
#def add_suffix(s):
#    '''This function adds the suffix '-Caltech' to the string s.'''
#    return s + '-Caltech'

#Ex. C.1.c: 's' in the return line should be changed to s. You're trying to add the
    # value of the variable s, not the string 's'.
#def add_suffix(s):
#    '''This function adds the suffix '-Caltech' to the string s.'''
#    return s + '-Caltech'

#Ex. C.1.d: String concatenation won't work because lst is not a string. Instead, use
    # the append() method on lst to append 'bam'.
#lst = ['foo', 'bar', 'baz']
#lst = lst.append('bam')

#Ex. C.1.e: The append() method doesn't return anything, it just appends an object
    # to a list. To fix this, return lst2 after appending 0.
#def reverse_and_append_zero(lst):
#    '''This function reverses a list of numbers and then
#    appends the number 0 to the end of the list.'''
#    lst2 = lst.reverse()
#    lst2.append(0)
#    return lst2

#Ex. C.1.f: str() is a function, not an object-- it can't be used as a variable name.
    # str is a reserved keyword. Change str to a non-reserved name.
#def append_string_letters_to_list(list, str_input):
#    '''
#    This function converts a string 'str' to a list and appends
#    the letters of the string to the list 'list'.
#    Example: 
#    >>> s = ['a', 'b']
#    >>> append_string_letters_to_list(s, 'cdef')
#    >>> s
#    ['a', 'b', 'c', 'd', 'e', 'f']
#    '''
#    letters = list(str_input)
#    list.append(letters)
    
#Ex. C.2: c has already been calculated as 10 + 20 = 30 by the time a has been redefined as 30.
#a = 10
#b = 20
#a = 30
#c = b + a
#print(c)

#Ex. C.3: Using add_and_double_1 would work because it returns a value you can set to a variable
    # or otherwise use elsewhere in your program. add_and_double_2 would not work because it 
    # simply prints the value instead of allowing you to use it somewhere else.

#Ex. C.4: Using sum_of_squares_1 would work because it calls for 2 arguments (which are
    # preferably numbers). Using sum_of_squares_2 would not work because in the example,
    # two arguments are supplied but sum_of_squares_2 asks for manual user input with the input()
    # function. Its signature does not ask for any input.

#Ex. C.5: Strings are immutable; after one is definied, you can't change just a single 
    # element of it. In order to change anything in the string, it must be redefined completely.
#def capitalize(s):
#    '''This function capitalizes the first letter of the string 's'.'''
#    s = s[0].upper() + s[1:len(s)]

#Ex. C.6: The list in the function is never actually changed, since the list variable is never assigned
    # to any element of the list.
#def double_list(lst):
#    '''This function doubles each element in a list in-place.'''
#    for i in range(len(lst)):
#        lst[i] *= 2

    
    
        