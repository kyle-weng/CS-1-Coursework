# Ex. A.1
class Point:
    '''This class represents a point in 3D space. Instances store three values:
        an x-coordinate, a y-coordinate, and a z-coordinate.'''
        
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def distanceTo(self, point2):
        '''Calculates and returns the distance between two points using
        Euclidean geometry.'''
        return (abs(self.x - point2.x) ** 2 + abs(self.y - point2.y) ** 2 + \
                abs(self.z - point2.z) ** 2) ** 0.5

# Ex. A.2
class Triangle:
    '''This class represents a triangle in 3D space. Instances store three Point
    objects representing the triangle's location.'''
    
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        
    def area(self):
        '''Calculates and returns the area of a triangle using Heron's
        formula.'''
        a = self.point1.distanceTo(self.point2)
        b = self.point2.distanceTo(self.point3)
        c = self.point3.distanceTo(self.point1)
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return area

# Ex. A.3
class Averager:
    '''This class stores a list of numbers and performs various operations on
    it.'''
    
    def __init__(self):
        self.nums = []
    
    def getNums(self):
        '''Returns the currently stored list of numbers.'''
        return self.nums[:]
    
    def append(self, newNumber):
        '''Appends a new number to the currently stored list of numbers.'''
        self.nums.append(newNumber)
        self.total = sum(self.nums)
        self.n = len(self.nums)
    
    def extend(self, newList):
        '''Extends a new list onto the currently stored list of numbers.'''
        self.nums.extend(newList)
        self.total = sum(self.nums)
        self.n = len(self.nums)
    
    def average(self):
        '''Computes the floating-point average of a stored list. If the list
        is empty, returns 0.0.'''
        if len(self.nums) == 0:
            return 0.0
        else:
            return (float(self.total) / self.n)
    
    def limits(self):
        '''Returns the minimum and maximum of the stored list. If the list is
        empty, it returns (0, 0).'''
        if len(self.nums) == 0:
            return (0, 0)
        else:
            return (min(self.nums), max(self.nums))

# Ex. B.1
# The "if-else" code structure is unnecessary. Instead, the function can just
# directly return the boolean result of the comparison.
def is_positive(x):
    '''Test if x is positive.'''
    return (x > 0)

# Ex. B.2
# The "for-each" loop is unnecessary; since the function is trying to return an
# index, a normal "for" loop would be more efficient.
def find(x, lst):
    '''Returns the index into a list where x is found, or -1 otherwise.
    Assume that x is found at most once in the list.'''
    for i in range(0, len(lst), 1):
        if lst[i] == x:
            return i
    return -1

# Ex. B.3
# The code should use elif statements to avoid having the program check multiple
# mutually exclusive if statements. As it is, the code is inefficient.
def categorize(x):
    '''Return a string categorizing the number 'x', which should be
    an integer.'''
    if x < 0:
        return 'negative'
    elif x == 0:
        return 'zero'
    elif x > 0 and x < 10:
        return 'small'
    elif x >= 10:
        return 'large'

# Ex. B.4
# THe use of if and elif statements results in unnecessary; the final elif 
# block works for all possible lengths of lst.
def sum_list(lst):
    '''Returns the sum of the elements of a list of numbers.'''
    total = 0
    for item in lst:
        total += item
    answer = total
    return answer

    