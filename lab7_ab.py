import sys
from math import exp

# Ex. A.1.1:
def union(set1, set2):
    '''Takes two sets and returns their union as another set.'''
    
    def conditionalAdd(add_from, add_to):
        '''Takes two sets and adds elements from the second to the first if
        those elements do not already exist in the first.'''
        
        for x in add_from:
            if x not in add_to:
                add_to.add(x)
        return add_to
    
    return conditionalAdd(set1, conditionalAdd(set2, set()))

# Ex. A.1.2:
def intersection(set1, set2):
    '''Takes two sets and returns their intersection as another set.'''
    
    to_return = set()
    for x in set2:
        if x in set1:
            to_return.add(x)
    return to_return

# Ex. A.1.3:
def difference(set1, set2):
    '''Takes two sets and returns their difference (all elements present in the
    first set but not the second) as another set.'''
    
    to_return = set()
    for x in set1:
        if x not in set2:
            to_return.add(x)
    return to_return

# Ex. A.2:
def mySum(*x):
    '''Takes an arbitrary number of positive integers and returns their sum.
    Raises a TypeError if an argument is not an integer. Raises a ValueError
    if an argument is less than 1.'''
    
    for z in x:
        try:
            assert int(z) == z
        except:
            raise TypeError('All arguments must be integers.')
        try:
            assert z > 0
        except:
            raise ValueError('All arguments must be greater than 0.')
    return sum(x)

# Ex. A.3:
def myNewSum(*x):
    '''Takes either a single list or an arbitrary number of positive integers
    and returns their sum. Raises a TypeError if more than one list is passed, 
    if the list's elements are not integers, or if a list and individual values
    are passed. Raises a ValueError if any supplied integer is less than 1.'''
    
    def check(z):
        '''Check that the parameter is a positive integer.'''
        try:
            assert int(z) == z
        except:
            raise TypeError('All arguments in the list must be integers.')
        try:
            assert z > 0
        except:
            raise ValueError('All arguments in the list must be positive.')

    if len(x) > 1:
        for n in x:
            if type(n) == list:
                raise TypeError('Either positive integers or a single list \
must be passed.')
            else:
                check(n)
        return sum(x)
    if len(x) == 1 and type(x[0]) == list:
        for z in x[0]:
            check(z)
        return sum(x[0])
    elif len(x) == 1 and type(x[0]) == int:
        return x[0]
    else:
        return 0

# Ex. A.4:
def myOpReduce(x, **kw):
    '''Takes a list of integers and a string, respectively. There are three
    acceptable values for the string:
        '+' - the function will return the sum of the integers
        '*' - the function will return the product of the integers
        'max' - the function will return the maximum of the list
    The function will return a ValueError if the string is not acceptable or
    a TypeError if the second argument is not a string.'''
    
    if len(list(kw.keys())) > 1 or len(list(kw.keys())) == 0:
        raise ValueError('There must be one keyword argument.')
    elif list(kw.keys())[0] != 'op':
        raise ValueError("The keyword argument must be 'op'.")
    if type(kw['op']) != str:
        raise TypeError('The second argument must be a string.')
    if not (kw['op'] == '+' or kw['op'] == '*' or kw['op'] == 'max'):
        raise ValueError("The second argument must be '+', '*', or 'max'.")
    if kw['op'] == '+':
        return sum(x)
    elif kw['op'] == '*':
        product = 1
        for z in x:
            product *= z
        return product
    elif kw['op'] == 'max':
        if len(x) > 0:
            return max(x)
        else:
            return 0

# Ex. B.1:
# When you catch the exception, you should raise it to let the user know about
# the error before you quit.
def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2.'''
    try:
        return dict[key1] + dict[key2]
    except KeyError: 
        raise KeyError('key1 and key2 must be strings.')
        # This ensures that the user actually knows about the error.

# Ex. B.2:
# This doesn't actually raise an error; the program still continues afterwards.
def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2.'''
    try:
        return dict[key1] + dict[key2]
    except KeyError:   # raised if a key isn't in a dictionary
        raise KeyError('key not found!')
        # This actually raises an error.

# Ex. B.3:
# When the KeyError is raised, it should also come with a message specifying
# what went wrong.
def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2.'''
    try:
        return dict[key1] + dict[key2]
    except KeyError:   # raised if a key isn't in a dictionary
        raise KeyError('key not found!')
        # This specifies what went wrong.

# Ex. B.4:
# When the KeyError is raised, it should specify which key is invalid.
def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2.'''
    try:
        val1 = dict[key1]
    except KeyError:   
        raise KeyError('key1 is invalid.')

    try:
        val2 = dict[key2]
    except KeyError:
        raise KeyError('key2 is invalid.')
    # The messages specify which key is problematic.
    
    return val1 + val2

# Ex. B.5:
# The error is raised before the message is printed, which means that the user
# doesn't ever see that message.
def fib(n):
    '''Return the nth fibonacci number.'''
    if n < 0:
        raise ValueError('n must be >= 0')
    elif n < 2:
        return n  # base cases: fib(0) = 0, fib(1) = 1.
    else:
        return fib(n-1) + fib(n-2)
    # By bundling the mssage with the raising, the user sees it.

# Ex. B.6:
# Printing the error before raising the actual error object is pointless because
# there is only one error that can be potentially handled in the function.
def fib(n):
    '''Return the nth fibonacci number.'''
    if n < 0:
        raise ValueError('n must be >= 0')
    elif n < 2:
        return n  # base cases: fib(0) = 0, fib(1) = 1.
    else:
        return fib(n-1) + fib(n-2)
    # By bundling the mssage with the raising, the user sees it.

# Ex. B.7:
# The error should be a ValueError, not a TypeError. It concerns the value of x.
def exp_x_over_x(x):
    '''
    Return the value of e**x / x, for x > 0.0 and
    e = 2.71828... (base of natural logarithms).
    '''
    if x <= 0.0:
        raise ValueError('x must be > 0.0') #now it's a ValueError
    return (exp(x) / x)

# Ex. B.8:
# Instead of raising generic Exceptions, specific types of errors should be
# raised.
def exp_x_over_x(x):
    '''
    Return the value of e**x / x, for x > 0.0 and
    e = 2.71828... (base of natural logarithms).
    '''
    if type(x) is not float:
        raise TypeError('x must be a float')
    elif x <= 0.0:
        raise ValueError('x must be > 0.0')
    return (exp(x) / x)
    # The generic Exceptions have been changed to specific errors.



    
                    
        
                    