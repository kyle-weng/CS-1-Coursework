#Ex. C.1.1: 6
#Ex. C.1.2: 20.0
#Ex. C.1.3: 4.5
#Ex. C.1.4: -4.5
#Ex. C.1.5: 1
#Ex. C.1.6: -1
#Ex. C.1.7: 1
#Ex. C.1.8: -4.5
#Ex. C.1.9: 19
#Ex. C.1.10: 35

#Ex. C.2.1: 100
#Ex. C.2.2: 110
#Ex. C.2.3: 130
#Ex. C.2.4: 90
#Ex. C.2.5: 40
#Ex. C.2.6: 120
#Ex. C.2.7: 24.0
#Ex. C.2.8: 0.0

#Ex. C.3:
#1. The expression on the right hand side of the leftmost operator is evaluated. 
    #In this case, x - x = 3 - 3 = 0.
#2. Because the leftmost operator is +=, this quantity (0) is added to x. x += 0
    #results in x = 3, because 3 + 0 = 3. After this statement has been evaluated,
    #the value of x is 3.

#Ex. C.4.1: 3.4j
#Ex. C.4.2: (-16+0j)
#Ex. C.4.3: (0.44+0.08j)
#Ex. C.4.1: (-3+4j)
#Ex. C.4.2: (1+4j)
#The last two expressions give different results because Python pays attention
    #to the order of operations; in this case, it evaluates the expressions 
    #inside parentheses first. Python does not automatically group expressions 
    #of multiple complex numbers into their constituents.

#Ex. C.5.1: (-3.165778513216168+1.9596010414216063j)
#Ex. C.5.2: (1.2652585805200263+1.856847768512215j)
#Ex. C.5.3: (-1-1.2246467991473532e-16j)
#Importing with a wildcard allows for unqualified usage of any function in the 
    #imported module. If two modules have identically named functions, importing 
    #the modules with wildcards will cause a name clash-- only the more recently 
    #imported function will be usable. If the modules are imported such that 
    #qualifying their names are required to call their functions, then name 
    #clashes will not happen.

#Ex. C.6.1: 'foobar'
#Ex. C.6.2: 'foobar'
#Ex. C.6.3: 'foobar'
#Ex. C.6.4: SyntaxError: unexpected EOF while parsing

#Ex. C.7: 'A\nB\nC'

#Ex. C.8: 80 * '-'

#Ex. C.9: 'first line\nsecond line\nthird line'

x = 3
y = 12.5
#Ex. C.10.1:
print("The rabbit is {}.".format(x))
#Ex. C.10.2:
print("The rabbit is {} years old.".format(x))
#Ex. C.10.3:
print("{} is average.".format(y))
#Ex. C.10.4:
print("{0} * {1}".format(y,x))
#Ex. C.10.5:
print("{0} * {1} is {2}".format(y,x,y*x))

#Ex. C.11:
num = float(input("Enter a number: "))
print(num)

#Ex. C.12:
def quadratic(a, b, c, x):
    return (a * x ** 2 + b * x + c)

#Ex. C.13:
def GC_content(input_string):
    '''Given an input string representing a DNA sequence, this function returns 
    the proportion of bases within the sequence that are either G or C.'''
    return ((input_string.count('G') + input_string.count('C')) / len(input_string))