'''
The CS 1 final exam, Fall 2018, part 1.

Functions on locations and sets of locations.
'''

import string
from utils import *

def is_adjacent(loc1, loc2):
    '''
    Arguments:
      loc1, loc2 -- (row, column) locations

    Return value: 
      True if two locations are orthogonally adjacent, otherwise False.
    '''

    assert is_loc(loc1)
    assert is_loc(loc2)
    
    adjacent_vertical = abs(loc1[0] - loc2[0])
    adjacent_horizontal = abs(loc1[1] - loc2[1])
    
    return adjacent_vertical + adjacent_horizontal == 1

def adjacent_to_any(loc, locset):
    '''
    Arguments:
      loc -- a (row, column) location
      locset -- a set of locations

    Return value:
      True if `loc` is not in `locset` and at least one location 
      in `locset` is adjacent to `loc`, otherwise False.

    The set `locset` is not altered.
    '''
    assert is_loc(loc)
    assert is_locset(locset)
    
    return (True in [is_adjacent(loc,loc2) for loc2 in locset] and loc not in\
locset)

def collect_adjacent(locset, target_set):
    '''
    Arguments:
      locset -- a set of (row, column) locations
      target_set -- another set of (row, column) locations

    Return value: 
      A set of all the locations in `locset` that are adjacent 
      to any location in `target_set`.

    The sets `locset` and `target_set` are not altered.
    '''

    assert is_locset(locset)
    assert is_locset(target_set)
    
    result = set()
    for loc in locset:
        if adjacent_to_any(loc,target_set):
            result.add(loc)
    return result

def collect_connected(loc, locset):
    '''
    Arguments:
      loc -- a (row, column) location
      locset -- a set of locations

    Return value: 
      A set of all the locations in `locset` which are connected to `loc` 
      via a chain of adjacent locations. Include `loc` in the resulting set.

    The set `locset` is not altered.
    '''
    
    assert is_loc(loc)
    assert is_locset(locset)
    locset_copy = locset.copy()
    if loc in locset_copy:
        locset_copy.remove(loc)
    result = {loc}
    while (collect_adjacent(result,locset_copy) != set()):
        collected_result = collect_adjacent(locset_copy,result)
        for x in collected_result:
            result.add(x)
            locset_copy.remove(x)
    
    return result

def partition_connected(locset):
    '''
    Partition a set of locations based on being connected via a chain of
    adjacent locations.  The original locset is not altered.
    Return a list of subsets.  The subsets must all be disjoint i.e.
    the intersection of any two subsets must be the empty set.

    Arguments:
      locset -- a set of (row, column) locations

    Return value: 
      The list of partitioned subsets.

    The set `locset` is not altered.
    '''

    assert is_locset(locset)
    
    result = []
    locset_copy = locset.copy()
    for x in locset_copy:
        locset_copy_exclusive = locset_copy.copy()
        locset_copy_exclusive.remove(x)
        subresult = collect_connected(x,locset_copy_exclusive)
        if subresult not in result:
            result.append(subresult)
    
    return result
    
        

def filter_locset(locset):
    '''
    Given a locset, partition it into subsets which are connected via a
    chain of adjacent locations.  Compute two sets:
      -- the union of all partitions whose length is < 3 
      -- the union of all partitions whose length is >= 3 
    and return them as a tuple of two sets (in that order).  

    Arguments:
      locset -- a set of (row, column) locations

    Return value:
      The two sets as described above.

    The set `locset` is not altered.
    '''

    assert is_locset(locset)
    
    less_three = set()
    ge_three = set()
    x = partition_connected(locset)
    for z in x:
        if len(z) >= 3:
            ge_three.update(z)
        else:
            less_three.update(z)
    return(less_three,ge_three)


