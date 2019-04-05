import random as r
import traceback as tb
import locset as ls
import utils as u

NTESTS = 100

# ---------------------------------------------------------------------- 
# Test framework.
# ---------------------------------------------------------------------- 

# Global variables.
ntests = 0
test_failures = 0
test_successes = 0

def reset_test_counts():
    '''
    Reset the test counter variables to 0.
    '''

    global ntests, test_failures, test_successes
    ntests = 0
    test_failures = 0
    test_successes = 0

def run_test(testfunc):
    '''
    Run a test.  Catch and display any tracebacks.
    Update test statistics.

    Arguments:
      testfunc -- the test function

    Return value: none

    Side effects:
      The global variables 'ntests', 'test_failures', and 'test_successes'
      may be updated.
    '''

    global ntests, test_failures, test_successes
    print('{} ... '.format(testfunc.__name__), end='')
    ntests += 1
    try:
        testfunc()
    except AssertionError as e:
        traceback_str = ''.join(tb.format_tb(e.__traceback__))
        print()
        print('-' * 70)
        print(traceback_str.strip())
        print('-' * 70)
        test_failures += 1
        print('test failed\n')
        return
    test_successes += 1
    print('passed')

def wrap_up():
    '''Print overall test results.'''
    print(f'Number of tests:  {ntests:4}')
    print(f'Tests passed:     {test_successes:4}')
    print(f'Tests failed:     {test_failures:4}')
    print()

def lists_equal(lst1, lst2):
    '''
    Return True if `lst1` and `lst2` have the same length and contain
    the same elements.  The order of the elements in the list doesn't
    matter.  This assumes that all list elements are distinct.
    '''

    if len(lst1) != len(lst2):
        return False
    for item in lst1:
        if item not in lst2:
            return False
    for item in lst2:
        if item not in lst1:
            return False
    return True

# ---------------------------------------------------------------------- 
# Generators.
# ---------------------------------------------------------------------- 

def make_random_loc(nrows, ncols):
    ''' Create a random loc. '''
    row = r.randrange(nrows)
    col = r.randrange(ncols)
    return (row, col)

def make_random_locset(nlocs, nrows, ncols):
    ''' Create a random locset. '''
    locs = set()
    while len(locs) < nlocs:
        locs.add(make_random_loc(nrows, ncols))
    return locs

# ---------------------------------------------------------------------- 
# Tests.
# ---------------------------------------------------------------------- 

def test_is_adjacent():
    # Generated tests:
    assert ls.is_adjacent((0, 0), (0, 1))
    assert ls.is_adjacent((0, 1), (0, 0))
    assert ls.is_adjacent((0, 1), (1, 1))
    assert ls.is_adjacent((0, 2), (0, 1))
    assert ls.is_adjacent((0, 3), (1, 3))
    assert ls.is_adjacent((1, 0), (2, 0))
    assert ls.is_adjacent((1, 1), (0, 1))
    assert ls.is_adjacent((1, 1), (1, 0))
    assert ls.is_adjacent((1, 1), (1, 2))
    assert ls.is_adjacent((1, 1), (2, 1))
    assert ls.is_adjacent((1, 2), (0, 2))
    assert ls.is_adjacent((2, 1), (1, 1))
    assert ls.is_adjacent((2, 2), (2, 3))
    assert ls.is_adjacent((2, 3), (2, 2))
    assert ls.is_adjacent((3, 1), (3, 2))
    assert ls.is_adjacent((3, 2), (2, 2))
    assert ls.is_adjacent((3, 2), (3, 1))
    assert ls.is_adjacent((4, 1), (4, 0))
    assert ls.is_adjacent((4, 2), (3, 2))
    assert ls.is_adjacent((4, 3), (4, 2))
    assert not ls.is_adjacent((0, 0), (0, 0))
    assert not ls.is_adjacent((0, 0), (0, 2))
    assert not ls.is_adjacent((0, 3), (0, 0))
    assert not ls.is_adjacent((1, 1), (0, 0))
    assert not ls.is_adjacent((1, 1), (0, 2))
    assert not ls.is_adjacent((1, 1), (1, 1))
    assert not ls.is_adjacent((1, 1), (2, 0))
    assert not ls.is_adjacent((1, 1), (2, 2))
    assert not ls.is_adjacent((1, 2), (3, 2))
    assert not ls.is_adjacent((1, 3), (0, 2))
    assert not ls.is_adjacent((2, 0), (0, 3))
    assert not ls.is_adjacent((2, 2), (0, 0))
    assert not ls.is_adjacent((2, 2), (0, 3))
    assert not ls.is_adjacent((2, 3), (1, 1))
    assert not ls.is_adjacent((3, 0), (1, 3))
    assert not ls.is_adjacent((3, 0), (4, 2))
    assert not ls.is_adjacent((3, 1), (0, 0))
    assert not ls.is_adjacent((3, 3), (1, 3))
    assert not ls.is_adjacent((4, 0), (0, 0))
    assert not ls.is_adjacent((4, 2), (0, 0))
    assert not ls.is_adjacent((4, 2), (0, 0))

def test_adjacent_to_any():
    # Test invariant:
    # A loc argument which is in the locset argument
    # always gives a False result.
    for _ in range(NTESTS):
        nlocs1 = r.randrange(1, 5)
        l1 = make_random_locset(nlocs1, 5, 4)
        for elem in l1:
            assert not ls.adjacent_to_any(elem, l1)

    # Generated tests:
    assert ls.adjacent_to_any((0, 2), {(1, 2), (2, 3), (3, 0), (4, 2), (2, 1)})
    assert ls.adjacent_to_any((0, 2), {(0, 1), (3, 0), (1, 0), (4, 1), (4, 0)})
    assert ls.adjacent_to_any((0, 3), {(4, 3), (1, 0), (4, 1), (0, 2), (4, 0)})
    assert ls.adjacent_to_any((1, 0), {(1, 2), (1, 3), (0, 0), (3, 3), (1, 1)})
    assert ls.adjacent_to_any((1, 0), {(0, 1), (3, 2), (0, 0), (4, 2), (0, 3)})
    assert ls.adjacent_to_any((1, 1), {(1, 2), (2, 3), (1, 0), (2, 1), (0, 3)})
    assert ls.adjacent_to_any((1, 2), {(3, 2), (4, 2), (0, 3), (4, 1), (1, 1)})
    assert ls.adjacent_to_any((1, 3), {(1, 2), (2, 0), (1, 1), (4, 3), (0, 2)})
    assert ls.adjacent_to_any((2, 0), {(0, 0), (3, 0), (4, 2), (0, 3), (1, 1)})
    assert ls.adjacent_to_any((2, 1), {(2, 3), (3, 3), (4, 3), (2, 2), (1, 1)})
    assert ls.adjacent_to_any((2, 2), {(3, 2), (4, 3), (3, 0), (4, 2), (4, 1)})
    assert ls.adjacent_to_any((2, 2), {(1, 3), (4, 2), (1, 0), (2, 1), (4, 0)})
    assert ls.adjacent_to_any((2, 2), {(1, 2), (3, 3), (3, 0), (0, 2), (4, 0)})
    assert ls.adjacent_to_any((2, 2), {(0, 0), (2, 3), (3, 3), (3, 0), (0, 3)})
    assert ls.adjacent_to_any((3, 0), {(1, 2), (3, 2), (4, 1), (0, 2), (4, 0)})
    assert ls.adjacent_to_any((3, 2), {(2, 0), (1, 3), (2, 2), (3, 1), (4, 0)})
    assert ls.adjacent_to_any((3, 3), {(2, 0), (0, 0), (4, 3), (3, 1), (2, 1)})
    assert ls.adjacent_to_any((3, 3), {(0, 1), (1, 3), (0, 0), (2, 3), (1, 0)})
    assert ls.adjacent_to_any((4, 2), {(0, 1), (4, 3), (3, 0), (4, 1), (0, 2)})
    assert ls.adjacent_to_any((4, 2), {(1, 2), (4, 3), (3, 0), (0, 3), (4, 1)})
    assert not ls.adjacent_to_any((0, 0), {(1, 2), (1, 3), (3, 3), (0, 3), (0, 2)})
    assert not ls.adjacent_to_any((0, 0), {(3, 2), (2, 3), (2, 2), (3, 0), (1, 1)})
    assert not ls.adjacent_to_any((0, 1), {(1, 2), (0, 1), (3, 3), (3, 0), (0, 2)})
    assert not ls.adjacent_to_any((0, 3), {(3, 2), (2, 3), (4, 3), (0, 3), (3, 1)})
    assert not ls.adjacent_to_any((1, 0), {(1, 3), (2, 3), (1, 0), (3, 1), (4, 1)})
    assert not ls.adjacent_to_any((1, 1), {(1, 3), (4, 3), (4, 2), (0, 3), (4, 1)})
    assert not ls.adjacent_to_any((1, 1), {(3, 3), (4, 3), (3, 0), (4, 1), (4, 0)})
    assert not ls.adjacent_to_any((2, 0), {(2, 0), (0, 0), (1, 3), (4, 3), (0, 3)})
    assert not ls.adjacent_to_any((2, 2), {(0, 1), (0, 0), (2, 3), (3, 3), (2, 2)})
    assert not ls.adjacent_to_any((2, 3), {(1, 2), (3, 2), (2, 3), (4, 1), (4, 0)})
    assert not ls.adjacent_to_any((3, 1), {(2, 0), (3, 3), (1, 0), (0, 2), (0, 3)})
    assert not ls.adjacent_to_any((3, 2), {(0, 1), (3, 2), (2, 3), (1, 0), (4, 0)})
    assert not ls.adjacent_to_any((4, 0), {(1, 2), (2, 2), (1, 0), (3, 1), (2, 1)})
    assert not ls.adjacent_to_any((4, 0), {(2, 0), (0, 0), (3, 0), (4, 1), (4, 0)})
    assert not ls.adjacent_to_any((4, 0), {(1, 3), (2, 2), (4, 2), (0, 3), (0, 2)})
    assert not ls.adjacent_to_any((4, 1), {(0, 1), (4, 3), (2, 2), (1, 1), (2, 1)})
    assert not ls.adjacent_to_any((4, 1), {(0, 1), (3, 2), (2, 3), (3, 3), (0, 2)})
    assert not ls.adjacent_to_any((4, 1), {(2, 0), (4, 2), (0, 3), (4, 1), (2, 1)})
    assert not ls.adjacent_to_any((4, 1), {(1, 2), (0, 3), (4, 1), (0, 2), (4, 0)})
    assert not ls.adjacent_to_any((4, 3), {(0, 1), (2, 3), (4, 3), (3, 0), (3, 1)})
    assert not ls.adjacent_to_any((4, 3), {(0, 1), (2, 3), (4, 3), (3, 0), (3, 1)})

def test_collect_adjacent():
    # Test invariants:
    # 1) Calling `collect_adjacent` doesn't change the input locsets
    # 2) The output is a locset
    for _ in range(NTESTS):
        nlocs1 = r.randrange(1, 5)
        l1 = make_random_locset(nlocs1, 5, 4)
        l1_copy = l1.copy()
        nlocs2 = r.randrange(1, 5)
        l2 = make_random_locset(nlocs2, 5, 4)
        l2_copy = l2.copy()
        l3 = ls.collect_adjacent(l1, l2)
        l4 = ls.collect_adjacent(l2, l1)
        assert u.is_locset(l3)
        assert u.is_locset(l4)
        assert l1 == l1_copy  # l1 hasn't changed
        assert l2 == l2_copy  # l2 hasn't changed

    # Generated tests:
    assert ls.collect_adjacent({(3, 1), (4, 1), (4, 0)}, {(1, 0), (0, 3), (0, 0)}) == set()
    assert ls.collect_adjacent({(3, 1), (3, 3), (4, 3)}, {(1, 0), (2, 2)}) == set()
    assert ls.collect_adjacent({(3, 0), (4, 0)}, {(4, 2), (1, 3)}) == set()
    assert ls.collect_adjacent({(0, 1), (4, 2)}, {(1, 2), (3, 0), (0, 2), (2, 1), (4, 0)}) == {(0, 1)}
    assert ls.collect_adjacent({(1, 3), (0, 0), (4, 3)}, {(3, 2), (3, 1), (0, 2), (0, 3)}) == {(1, 3)}
    assert ls.collect_adjacent({(1, 2), (1, 3), (1, 0), (4, 1), (1, 1)}, {(0, 3), (4, 3)}) == {(1, 3)}
    assert ls.collect_adjacent({(1, 0), (2, 2)}, {(3, 0), (3, 1), (1, 1), (4, 3)}) == {(1, 0)}
    assert ls.collect_adjacent({(0, 1), (4, 3), (2, 2), (3, 0), (0, 2)}, {(4, 2), (2, 2)}) == {(4, 3)}
    assert ls.collect_adjacent({(0, 0), (2, 3)}, {(4, 2), (2, 0), (2, 2)}) == {(2, 3)}
    assert ls.collect_adjacent({(4, 2), (1, 0), (3, 3)}, {(4, 1), (4, 0)}) == {(4, 2)}
    assert ls.collect_adjacent({(0, 3), (2, 1)}, {(3, 0), (4, 2), (3, 1), (0, 0)}) == {(2, 1)}
    assert ls.collect_adjacent({(0, 3), (3, 1)}, {(3, 0), (1, 3), (4, 3)}) == {(0, 3), (3, 1)}
    assert ls.collect_adjacent({(3, 0), (4, 2), (2, 1)}, {(3, 2), (4, 0)}) == {(3, 0), (4, 2)}
    assert ls.collect_adjacent({(2, 3), (1, 1)}, {(1, 2), (0, 1), (4, 3), (2, 2), (0, 2)}) == {(2, 3), (1, 1)}
    assert ls.collect_adjacent({(0, 0), (3, 3), (4, 3), (1, 0), (1, 1)}, {(0, 1), (3, 1), (4, 1), (0, 2)}) == {(0, 0), (1, 1)}
    assert ls.collect_adjacent({(0, 1), (0, 3)}, {(1, 3), (2, 3), (1, 1), (4, 3)}) == {(0, 1), (0, 3)}
    assert ls.collect_adjacent({(4, 3), (1, 0), (3, 1), (4, 1), (4, 0)}, {(1, 3), (4, 1), (2, 1), (2, 3)}) == {(3, 1), (4, 0)}
    assert ls.collect_adjacent({(2, 0), (3, 1), (0, 2), (4, 3)}, {(3, 0), (3, 2), (1, 3), (1, 1)}) == {(2, 0), (3, 1)}
    assert ls.collect_adjacent({(0, 1), (1, 2), (3, 2), (3, 0), (4, 1)}, {(3, 0), (4, 2), (2, 3)}) == {(3, 2), (4, 1)}
    assert ls.collect_adjacent({(0, 1), (4, 3), (2, 2), (3, 1), (0, 2)}, {(3, 2), (2, 3), (0, 2)}) == {(0, 1), (3, 1), (2, 2)}
    assert ls.collect_adjacent({(0, 1), (4, 3), (2, 2), (3, 1), (0, 2)}, {(3, 2), (2, 3), (0, 2)}) == {(0, 1), (3, 1), (2, 2)}

def test_collect_connected():
    # Test invariants:
    # 1) Calling `collect_connected` doesn't change the input locset
    # 2) The output is a locset
    # 3) The argument item is always in the output locset
    # 4) The output locset minus the input loc is a subset of the input locset
    for _ in range(NTESTS):
        nlocs = r.randrange(1, 5)
        l1 = make_random_locset(nlocs, 5, 4)
        l1_copy = l1.copy()
        loc = make_random_loc(5, 4)
        l2 = ls.collect_connected(loc, l1)
        assert l1 == l1_copy  # l1 hasn't changed
        assert u.is_locset(l2)
        assert loc in l2
        l3 = l2.copy()
        l3.remove(loc)
        assert l3.issubset(l1)

    # Generated tests:
    assert ls.collect_connected((3, 0), {(1, 3), (0, 0), (2, 3), (3, 0), (0, 3)}) == {(3, 0)}
    assert ls.collect_connected((4, 2), {(1, 2), (1, 3), (3, 3), (2, 2), (3, 1)}) == {(4, 2)}
    assert ls.collect_connected((2, 3), {(3, 2), (0, 0), (0, 3), (3, 1), (1, 1)}) == {(2, 3)}
    assert ls.collect_connected((0, 3), {(0, 1), (2, 3), (3, 3), (1, 1), (2, 1)}) == {(0, 3)}
    assert ls.collect_connected((3, 0), {(1, 3), (2, 3), (4, 3), (4, 2), (4, 1)}) == {(3, 0)}
    assert ls.collect_connected((2, 1), {(1, 3), (0, 0), (0, 3), (3, 1), (2, 1)}) == {(3, 1), (2, 1)}
    assert ls.collect_connected((4, 2), {(0, 1), (2, 0), (3, 0), (4, 1), (1, 1)}) == {(4, 2), (4, 1)}
    assert ls.collect_connected((1, 2), {(0, 0), (1, 3), (3, 0), (4, 2), (3, 1)}) == {(1, 2), (1, 3)}
    assert ls.collect_connected((3, 0), {(0, 1), (2, 0), (1, 3), (4, 3), (0, 3)}) == {(3, 0), (2, 0)}
    assert ls.collect_connected((1, 3), {(2, 0), (1, 3), (4, 3), (0, 3), (4, 1)}) == {(0, 3), (1, 3)}
    assert ls.collect_connected((3, 1), {(4, 2), (0, 3), (3, 1), (4, 1), (0, 2)}) == {(4, 2), (3, 1), (4, 1)}
    assert ls.collect_connected((0, 2), {(0, 1), (1, 2), (3, 2), (2, 0), (3, 3)}) == {(0, 1), (0, 2), (1, 2)}
    assert ls.collect_connected((4, 1), {(2, 0), (4, 3), (4, 2), (4, 1), (0, 2)}) == {(4, 2), (4, 1), (4, 3)}
    assert ls.collect_connected((3, 0), {(0, 1), (4, 2), (1, 0), (3, 1), (2, 1)}) == {(3, 0), (3, 1), (2, 1)}
    assert ls.collect_connected((3, 2), {(0, 1), (1, 2), (1, 3), (0, 0), (2, 2)}) == {(1, 2), (3, 2), (1, 3), (2, 2)}
    assert ls.collect_connected((0, 2), {(1, 2), (1, 3), (3, 3), (2, 2), (4, 1)}) == {(1, 2), (1, 3), (0, 2), (2, 2)}
    assert ls.collect_connected((0, 1), {(1, 2), (1, 1), (3, 3), (4, 2), (0, 2)}) == {(0, 1), (1, 1), (0, 2), (1, 2)}
    assert ls.collect_connected((2, 2), {(1, 2), (2, 0), (3, 2), (1, 3), (4, 2)}) == {(1, 2), (3, 2), (1, 3), (2, 2), (4, 2)}
    assert ls.collect_connected((3, 0), {(2, 0), (4, 2), (1, 0), (1, 1), (2, 1)}) == {(2, 0), (3, 0), (1, 0), (1, 1), (2, 1)}
    assert ls.collect_connected((3, 1), {(2, 0), (3, 3), (1, 0), (4, 1), (2, 1)}) == {(2, 0), (1, 0), (3, 1), (4, 1), (2, 1)}
    assert ls.collect_connected((3, 1), {(2, 0), (3, 3), (1, 0), (4, 1), (2, 1)}) == {(2, 0), (1, 0), (3, 1), (4, 1), (2, 1)}

def test_partition_connected():
    # Test invariants:
    # 1) Calling `partition_connected` doesn't change the input locset
    # 2) The output is a list of locsets.
    # 3) None of the locsets in the output list are empty.
    # 4) The output locsets must all be disjoint.
    # 5) The union of the output locsets must equal the input locset.
    for _ in range(NTESTS):
        nlocs = r.randrange(7, 15)
        l1 = make_random_locset(nlocs, 5, 4)
        l1_copy = l1.copy()
        l2 = ls.partition_connected(l1)
        assert l1 == l1_copy  # l1 hasn't changed
        assert type(l2) is list
        for item in l2:
            assert u.is_locset(item)
            assert item != set()  # not the empty set
        assert u.disjoint_subsets(l2)
        assert set().union(*l2) == l1

    # Generated tests:
    assert lists_equal(ls.partition_connected({(2, 0), (1, 3), (3, 3), (0, 2), (1, 1)}), [{(2, 0)}, {(0, 2)}, {(1, 3)}, {(1, 1)}, {(3, 3)}])
    assert lists_equal(ls.partition_connected({(2, 2), (1, 0), (3, 1), (0, 2), (0, 3)}), [{(2, 2)}, {(1, 0)}, {(0, 3), (0, 2)}, {(3, 1)}])
    assert lists_equal(ls.partition_connected({(2, 0), (3, 2), (1, 3), (4, 3), (2, 1)}), [{(2, 0), (2, 1)}, {(3, 2)}, {(1, 3)}, {(4, 3)}])
    assert lists_equal(ls.partition_connected({(2, 3), (4, 3), (1, 1), (2, 1), (4, 0)}), [{(2, 3)}, {(1, 1), (2, 1)}, {(4, 3)}, {(4, 0)}])
    assert lists_equal(ls.partition_connected({(2, 3), (3, 0), (4, 2), (1, 0), (0, 2), (2, 1)}), [{(2, 3)}, {(3, 0)}, {(4, 2)}, {(1, 0)}, {(0, 2)}, {(2, 1)}])
    assert lists_equal(ls.partition_connected({(3, 2), (0, 0), (3, 0), (4, 2), (4, 1), (4, 0)}), [{(3, 2), (3, 0), (4, 2), (4, 1), (4, 0)}, {(0, 0)}])
    assert lists_equal(ls.partition_connected({(2, 0), (3, 2), (1, 3), (3, 0), (0, 3), (3, 1), (0, 2)}), [{(3, 0), (2, 0), (3, 2), (3, 1)}, {(0, 3), (1, 3), (0, 2)}])
    assert lists_equal(ls.partition_connected({(3, 2), (0, 0), (2, 2), (3, 0), (0, 3), (4, 1), (1, 1)}), [{(3, 2), (2, 2)}, {(0, 0)}, {(3, 0)}, {(0, 3)}, {(4, 1)}, {(1, 1)}])
    assert lists_equal(ls.partition_connected({(1, 2), (0, 0), (1, 3), (2, 3), (3, 0), (1, 0), (0, 2)}), [{(1, 2), (1, 3), (2, 3), (0, 2)}, {(3, 0)}, {(1, 0), (0, 0)}])
    assert lists_equal(ls.partition_connected({(0, 1), (1, 2), (2, 0), (4, 2), (0, 3), (4, 1), (1, 1)}), [{(0, 1), (1, 1), (1, 2)}, {(4, 2), (4, 1)}, {(2, 0)}, {(0, 3)}])
    assert lists_equal(ls.partition_connected({(3, 2), (0, 0), (1, 3), (3, 3), (3, 0), (4, 3), (0, 3), (0, 2)}), [{(3, 2), (3, 3), (4, 3)}, {(0, 3), (1, 3), (0, 2)}, {(3, 0)}, {(0, 0)}])
    assert lists_equal(ls.partition_connected({(3, 2), (1, 3), (3, 0), (3, 1), (2, 3), (1, 0), (4, 1), (0, 2)}), [{(3, 0), (3, 2), (3, 1), (4, 1)}, {(1, 0)}, {(1, 3), (2, 3)}, {(0, 2)}])
    assert lists_equal(ls.partition_connected({(1, 3), (3, 3), (3, 0), (2, 3), (4, 3), (2, 2), (1, 1), (4, 0)}), [{(1, 3), (2, 3), (3, 3), (4, 3), (2, 2)}, {(3, 0), (4, 0)}, {(1, 1)}])
    assert lists_equal(ls.partition_connected({(3, 2), (0, 0), (3, 0), (2, 2), (1, 0), (4, 1), (1, 1), (4, 0)}), [{(3, 2), (2, 2)}, {(1, 0), (0, 0), (1, 1)}, {(3, 0), (4, 1), (4, 0)}])
    assert lists_equal(ls.partition_connected({(1, 2), (3, 2), (3, 3), (0, 2), (3, 1), (2, 0), (4, 3), (2, 2), (1, 1)}), [{(1, 2), (3, 2), (3, 3), (4, 3), (2, 2), (0, 2), (3, 1), (1, 1)}, {(2, 0)}])
    assert lists_equal(ls.partition_connected({(1, 2), (3, 2), (0, 0), (1, 3), (3, 3), (2, 2), (0, 3), (4, 1), (1, 1)}), [{(1, 2), (3, 2), (1, 3), (3, 3), (2, 2), (0, 3), (1, 1)}, {(0, 0)}, {(4, 1)}])
    assert lists_equal(ls.partition_connected({(1, 2), (1, 3), (3, 3), (3, 1), (2, 1), (2, 0), (2, 3), (0, 2), (4, 0)}), [{(1, 2), (1, 3), (2, 3), (3, 3), (0, 2)}, {(2, 0), (3, 1), (2, 1)}, {(4, 0)}])
    assert lists_equal(ls.partition_connected({(3, 2), (1, 3), (0, 0), (3, 1), (2, 3), (2, 2), (1, 0), (1, 1), (4, 0)}), [{(3, 2), (1, 3), (2, 3), (2, 2), (3, 1)}, {(1, 0), (0, 0), (1, 1)}, {(4, 0)}])
    assert lists_equal(ls.partition_connected({(0, 1), (1, 3), (3, 3), (2, 0), (2, 3), (4, 3), (0, 3), (1, 1), (4, 0)}), [{(0, 1), (1, 1)}, {(1, 3), (2, 3), (3, 3), (4, 3), (0, 3)}, {(2, 0)}, {(4, 0)}])
    assert lists_equal(ls.partition_connected({(0, 1), (1, 3), (1, 0), (3, 1), (4, 3), (2, 2), (0, 3), (4, 1), (0, 2), (4, 0)}), [{(0, 1), (0, 3), (1, 3), (0, 2)}, {(3, 1), (4, 1), (4, 0)}, {(1, 0)}, {(4, 3)}, {(2, 2)}])
    assert lists_equal(ls.partition_connected({(0, 1), (1, 3), (1, 0), (3, 1), (4, 3), (2, 2), (0, 3), (4, 1), (0, 2), (4, 0)}), [{(0, 1), (0, 3), (1, 3), (0, 2)}, {(3, 1), (4, 1), (4, 0)}, {(1, 0)}, {(4, 3)}, {(2, 2)}])

def test_filter_locset():
    # Test invariants:
    # 1) Calling `filter_locset` doesn't change the input locset
    # 2) The output is a 2-tuple of locsets.
    # 3) The output subsets must be disjoint.
    # 4) The union of the output locsets must equal the input locset.
    # 5) The second output locset must not have 1 or 2 elements.
    for _ in range(NTESTS):
        nlocs = r.randrange(7, 15)
        l1 = make_random_locset(nlocs, 5, 4)
        l1_copy = l1.copy()
        l2 = ls.filter_locset(l1)
        assert l1 == l1_copy  # l1 hasn't changed
        assert type(l2) is tuple
        assert len(l2) == 2
        assert u.is_locset(l2[0])
        assert u.is_locset(l2[1])
        assert u.disjoint_subsets(list(l2))
        assert set().union(*l2) == l1
        assert len(l2[1]) not in [1, 2]

    # Generated tests:
    assert ls.filter_locset({(0, 1), (0, 0), (0, 4), (0, 3), (0, 2)}) == (set(), {(0, 1), (0, 0), (0, 4), (0, 3), (0, 2)})
    assert ls.filter_locset({(1, 2), (3, 2), (3, 3), (2, 2), (3, 0)}) == ({(3, 0)}, {(1, 2), (3, 2), (3, 3), (2, 2)})
    assert ls.filter_locset({(0, 0), (3, 3), (2, 2), (4, 4), (1, 1)}) == ({(0, 0), (3, 3), (2, 2), (4, 4), (1, 1)}, set())
    assert ls.filter_locset({(0, 1), (0, 0), (3, 3), (3, 4), (0, 2)}) == ({(3, 4), (3, 3)}, {(0, 1), (0, 0), (0, 2)})
    assert ls.filter_locset({(1, 2), (3, 0), (1, 0), (2, 1), (0, 3)}) == ({(1, 2), (3, 0), (1, 0), (2, 1), (0, 3)}, set())
    assert ls.filter_locset({(3, 2), (1, 3), (4, 2), (3, 1), (2, 1), (4, 0)}) == ({(1, 3), (4, 0)}, {(4, 2), (3, 2), (3, 1), (2, 1)})
    assert ls.filter_locset({(1, 2), (3, 3), (2, 2), (4, 2), (4, 1), (0, 2)}) == ({(4, 2), (4, 1), (3, 3)}, {(1, 2), (0, 2), (2, 2)})
    assert ls.filter_locset({(1, 2), (2, 0), (3, 2), (4, 3), (0, 3), (3, 1), (2, 1)}) == ({(1, 2), (0, 3), (4, 3)}, {(2, 0), (3, 2), (3, 1), (2, 1)})
    assert ls.filter_locset({(1, 3), (2, 3), (3, 3), (4, 3), (0, 3), (3, 1), (2, 1)}) == ({(3, 1), (2, 1)}, {(1, 3), (2, 3), (3, 3), (4, 3), (0, 3)})
    assert ls.filter_locset({(1, 2), (2, 2), (0, 2), (0, 3), (3, 1), (4, 1), (1, 1)}) == ({(3, 1), (4, 1)}, {(1, 2), (2, 2), (0, 2), (0, 3), (1, 1)})
    assert ls.filter_locset({(0, 1), (3, 2), (3, 0), (2, 3), (4, 3), (4, 2), (4, 1), (0, 2)}) == ({(0, 1), (3, 0), (2, 3), (0, 2)}, {(4, 2), (3, 2), (4, 1), (4, 3)})
    assert ls.filter_locset({(0, 0), (3, 0), (3, 1), (2, 0), (4, 2), (4, 1), (0, 2), (4, 0)}) == ({(0, 0), (0, 2)}, {(2, 0), (3, 0), (4, 2), (3, 1), (4, 1), (4, 0)})
    assert ls.filter_locset({(1, 2), (0, 1), (2, 1), (2, 3), (2, 2), (4, 1), (1, 1), (4, 0)}) == ({(4, 1), (4, 0)}, {(1, 2), (0, 1), (2, 3), (2, 2), (1, 1), (2, 1)})
    assert ls.filter_locset({(1, 2), (3, 2), (0, 0), (2, 0), (4, 3), (2, 2), (4, 1), (0, 2)}) == ({(2, 0), (0, 0), (4, 1), (4, 3)}, {(1, 2), (3, 2), (0, 2), (2, 2)})
    assert ls.filter_locset({(1, 3), (3, 0), (2, 0), (1, 1), (4, 3), (2, 2), (4, 2), (0, 2)}) == ({(2, 0), (1, 3), (1, 1), (4, 3), (2, 2), (3, 0), (4, 2), (0, 2)}, set())
    assert ls.filter_locset({(1, 2), (0, 0), (3, 3), (2, 1), (2, 0), (4, 2), (4, 1), (4, 0)}) == ({(1, 2), (2, 0), (0, 0), (3, 3), (2, 1)}, {(4, 2), (4, 1), (4, 0)})
    assert ls.filter_locset({(1, 2), (1, 3), (0, 0), (3, 3), (3, 1), (2, 1), (2, 0), (1, 1), (4, 0)}) == ({(0, 0), (3, 3), (4, 0)}, {(1, 2), (2, 0), (1, 3), (3, 1), (1, 1), (2, 1)})
    assert ls.filter_locset({(1, 2), (0, 1), (3, 1), (2, 1), (2, 0), (4, 2), (1, 0), (4, 1), (0, 3)}) == ({(1, 2), (0, 3), (0, 1)}, {(2, 0), (4, 2), (1, 0), (3, 1), (4, 1), (2, 1)})
    assert ls.filter_locset({(1, 2), (1, 3), (0, 0), (2, 1), (2, 3), (2, 2), (4, 2), (1, 0), (1, 1), (4, 0)}) == ({(4, 2), (4, 0)}, {(1, 2), (1, 3), (0, 0), (2, 1), (2, 3), (2, 2), (1, 0), (1, 1)})
    assert ls.filter_locset({(0, 1), (0, 0), (1, 3), (3, 0), (3, 1), (2, 0), (2, 3), (4, 2), (1, 0), (0, 3)}) == ({(4, 2)}, {(0, 1), (0, 0), (1, 3), (3, 0), (3, 1), (2, 0), (2, 3), (1, 0), (0, 3)})
    assert ls.filter_locset({(0, 1), (0, 0), (1, 3), (3, 0), (3, 1), (2, 0), (2, 3), (4, 2), (1, 0), (0, 3)}) == ({(4, 2)}, {(0, 1), (0, 0), (1, 3), (3, 0), (3, 1), (2, 0), (2, 3), (1, 0), (0, 3)})

# ---------------------------------------------------------------------- 
# Entry point.
# ---------------------------------------------------------------------- 

if __name__ == '__main__':
    reset_test_counts()

    tests = [
      test_is_adjacent,
      test_adjacent_to_any,
      test_collect_adjacent,
      test_collect_connected,
      test_partition_connected,
      test_filter_locset
    ]

    print()
    for test in tests:
        run_test(test)
    print()
    wrap_up()
