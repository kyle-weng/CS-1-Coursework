import random, sys, copy
import midterm as m

#
# PART 2.
#

### 2.1

def same_tictactoe(t1, t2):
    '''
    Return True if two string representations of a tictactoe board
    can be considered to be "the same".
    '''

    assert type(t1) is str
    assert type(t2) is str

    if t1 == t2:
        return True
    l1 = t1.split('\n')
    l2 = t2.split('\n')
    if len(l1) != len(l2):
        return False
    for i in range(len(l1)):
        line1 = l1[i].rstrip()
        line2 = l2[i].rstrip()
        if line1 != line2:
            return False
    return True

def test_draw_tictactoe():
    # Management apologizes for the long lines.
    ttt1 = '\n | |\n-+-+-\n | |\n-+-+-\n | | \n\n'
    ttt2 = '\n  |  |\n  |  |  \n--+--+--\n  |  |\n  |  |  \n--+--+--\n  |  |\n  |  |\n\n'
    ttt3 = '\n   |   |\n   |   |\n   |   |\n---+---+---\n   |   |\n   |   |\n   |   |\n---+---+---\n   |   |\n   |   |\n   |   |\n\n' 
    ttt4 = '\n    |    |\n    |    |\n    |    |\n    |    |\n----+----+----\n    |    |\n    |    |\n    |    |\n    |    |\n----+----+----\n    |    |\n    |    |\n    |    |\n    |    |\n\n'
    ttt5 = '\n     |     |\n     |     |\n     |     |\n     |     |\n     |     |\n-----+-----+-----\n     |     |\n     |     |\n     |     |\n     |     |\n     |     |\n-----+-----+-----\n     |     |\n     |     |\n     |     |\n     |     |\n     |     |\n\n'

    assert same_tictactoe(m.draw_tictactoe(1), ttt1)
    assert same_tictactoe(m.draw_tictactoe(2), ttt2)
    assert same_tictactoe(m.draw_tictactoe(3), ttt3)
    assert same_tictactoe(m.draw_tictactoe(4), ttt4)
    assert same_tictactoe(m.draw_tictactoe(5), ttt5)

### 2.2

def test_rps():
    assert m.rps('R', 'R') == 0
    assert m.rps('R', 'S') == 1
    assert m.rps('R', 'P') == 2

    assert m.rps('S', 'R') == 2
    assert m.rps('S', 'S') == 0
    assert m.rps('S', 'P') == 1

    assert m.rps('P', 'R') == 1
    assert m.rps('P', 'S') == 2
    assert m.rps('P', 'P') == 0

def test_rpslk_general(f):
    assert f('R', 'R') == 0
    assert f('R', 'S') == 1
    assert f('R', 'P') == 2
    assert f('R', 'L') == 1
    assert f('R', 'K') == 2

    assert f('S', 'R') == 2
    assert f('S', 'S') == 0
    assert f('S', 'P') == 1
    assert f('S', 'L') == 1
    assert f('S', 'K') == 2

    assert f('P', 'R') == 1
    assert f('P', 'S') == 2
    assert f('P', 'P') == 0
    assert f('P', 'L') == 2
    assert f('P', 'K') == 1

    assert f('L', 'R') == 2
    assert f('L', 'S') == 2
    assert f('L', 'P') == 1
    assert f('L', 'L') == 0
    assert f('L', 'K') == 1

    assert f('K', 'R') == 1
    assert f('K', 'S') == 1
    assert f('K', 'P') == 2
    assert f('K', 'L') == 2
    assert f('K', 'K') == 0

def test_rpslk():
    test_rpslk_general(m.rpslk)

def test_rpslk2():
    test_rpslk_general(m.rpslk2)

### 2.3

ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
suits = ['S', 'H', 'D', 'C']

# Non-consecutive ranks, for generating non-straights.
ranks_nc = [2, 4, 6, 7, 9, 10, 'Q', 'K', 'A']

def validate_hand(hand):
    '''
    Validate a Poker hand given ranks `rs`.
    '''

    assert type(hand) is list
    assert len(hand) == 5
    for card in hand:
        assert type(card) is tuple
        assert len(card) == 2
        assert card[0] in ranks
        assert card[1] in suits

def make_no_pair():
    '''Return a poker hand which is no pair.'''
    ranksA = ranks_nc[:]
    rs = random.sample(ranksA, 5)
    # This choice of suits guarantees that we don't have a flush:
    ss = random.sample(suits, 2) + \
           [random.choice(suits), random.choice(suits), random.choice(suits)]
    hand = list(zip(rs, ss))
    random.shuffle(hand)
    return hand

def make_one_pair():
    '''Return a poker hand which is one pair.'''
    ranksA = ranks[:]
    rr = random.sample(ranksA, 4)
    rs = [rr[0]] * 2 + rr[1:]
    ss = random.sample(suits, 2) + \
           [random.choice(suits), random.choice(suits), random.choice(suits)]
    hand = list(zip(rs, ss))
    random.shuffle(hand)
    return hand

def make_two_pair():
    '''Return a poker hand which is two pair.'''
    ranksA = ranks[:]
    rr = random.sample(ranksA, 3)
    rs = [rr[0]] * 2 + [rr[1]] * 2 + [rr[2]]
    ss = random.sample(suits, 2) + \
           random.sample(suits, 2) + [random.choice(suits)]
    hand = list(zip(rs, ss))
    random.shuffle(hand)
    return hand

def make_three_of_a_kind():
    '''Return a poker hand which is three of a kind.'''
    ranksA = ranks[:]
    rr = random.sample(ranksA, 3)
    rs = [rr[0]] * 3 + rr[1:]
    ss = random.sample(suits, 3) + random.choices(suits, k=2)
    hand = list(zip(rs, ss))
    random.shuffle(hand)
    return hand

def make_straight():
    '''Return a poker hand which is a straight.'''
    start = random.randint(0, 9)
    if start == 9:
        rs = ['A', 2, 3, 4, 5]
    else:
        rs = ranks[start:start+5]
    ss = ['S', 'H', 'D', 'C'] + [random.choice(suits)]
    random.shuffle(rs)
    random.shuffle(ss)
    hand = list(zip(rs, ss))
    return hand

def make_flush():
    '''Return a poker hand which is a flush.'''
    suit = random.choice(suits)
    rs = random.sample(ranks_nc, 5)
    hand = [(r, suit) for r in rs]
    random.shuffle(hand)
    return hand

def make_full_house():
    '''Return a poker hand which is a full house.'''
    ranksA = ranks[:]
    rr = random.sample(ranksA, 2)
    rs = [rr[0]] * 3 + [rr[1]] * 2
    ss = random.sample(suits, 3) * 3 + random.choices(suits, k=2)
    hand = list(zip(rs, ss))
    random.shuffle(hand)
    return hand

def make_four_of_a_kind():
    '''Return a poker hand which is four of a kind.'''
    ranksA = ranks[:]
    rr = random.sample(ranksA, 2)
    rs = [rr[0]] * 4 + [rr[1]]
    ss = ['S', 'H', 'D', 'C', random.choice(suits)]
    hand = list(zip(rs, ss))
    random.shuffle(hand)
    return hand

def make_straight_flush():
    '''Return a poker hand which is a straight.'''
    start = random.randint(0, 9)
    if start == 9:
        rs = ['A', 2, 3, 4, 5]
    else:
        rs = ranks[start:start+5]
    suit = random.choice(suits)
    hand = [(r, suit) for r in rs]
    random.shuffle(hand)
    return hand

NTESTS_POKER_RANK = 1000

def test_specific_poker_rank(make_poker_rank_function, result):
    '''
    Test the `poker_rank` function on a specific poker rank.

    Arguments:
      make_poker_rank_function: a function to generate that rank
      result: the expected result

    Return value: none.  If the function returns, the test succeeds.
    '''

    for _ in range(NTESTS_POKER_RANK):
        h = make_poker_rank_function()
        validate_hand(h)
        r = m.poker_rank(h)
        assert r == result

def test_no_pair():
    test_specific_poker_rank(make_no_pair, 'NP')

def test_one_pair():
    test_specific_poker_rank(make_one_pair, '1P')

def test_two_pair():
    test_specific_poker_rank(make_two_pair, '2P')

def test_three_of_a_kind():
    test_specific_poker_rank(make_three_of_a_kind, '3K')

def test_straight():
    test_specific_poker_rank(make_straight, 'ST')

def test_flush():
    test_specific_poker_rank(make_flush, 'FL')
 
def test_full_house():
    test_specific_poker_rank(make_full_house, 'FH')

def test_four_of_a_kind():
    test_specific_poker_rank(make_four_of_a_kind, '4K')

def test_straight_flush():
    test_specific_poker_rank(make_straight_flush, 'SF')

def test_poker_rank():
    '''Test the poker_rank function.'''

    test_no_pair()
    test_one_pair()
    test_two_pair()
    test_three_of_a_kind()
    test_straight()
    test_flush()
    test_full_house()
    test_four_of_a_kind()
    test_straight_flush()

#
# PART 3.
#

NTESTS_LIFE = 1000

def test_make_empty_board():
    for _ in range(NTESTS_LIFE):
        nrows = random.randint(4, 7)
        ncols = nrows + random.randint(-2, 2)
        b = m.make_empty_board(nrows, ncols)
        assert type(b) is list  # check that b is a list
        assert len(b) == nrows
        for r in range(nrows):
            assert type(b[r]) is list
            assert len(b[r]) == ncols
        for r in range(nrows):
            for c in range(ncols):
                assert b[r][c] == 0

        # check for aliasing.
        for _ in range(10):
            rr = random.randrange(0, nrows)
            cc = random.randrange(0, ncols)
            b[rr][cc] = 1
            # Check that other rows didn't see the change.
            for r in range(nrows):
                if r == rr:
                    assert b[r][cc] == 1
                else:
                    assert b[r][cc] == 0
            b[rr][cc] = 0

def test_make_empty_board_2():
    assert m.make_empty_board(4, 2) == \
        [[0, 0], [0, 0], [0, 0], [0, 0]]
    assert m.make_empty_board(4, 3) == \
        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert m.make_empty_board(4, 4) == \
        [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    assert m.make_empty_board(4, 5) == \
        [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    assert m.make_empty_board(4, 6) == \
        [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    assert m.make_empty_board(5, 3) == \
        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert m.make_empty_board(5, 4) == \
        [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    assert m.make_empty_board(5, 5) == \
        [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    assert m.make_empty_board(5, 6) == \
        [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    assert m.make_empty_board(5, 7) == \
        [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    assert m.make_empty_board(6, 4) == \
        [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    assert m.make_empty_board(6, 5) == \
        [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    assert m.make_empty_board(6, 6) == \
        [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    assert m.make_empty_board(6, 7) == \
        [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    assert m.make_empty_board(6, 8) == \
        [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
    assert m.make_empty_board(7, 5) == \
        [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    assert m.make_empty_board(7, 6) == \
        [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    assert m.make_empty_board(7, 7) == \
        [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    assert m.make_empty_board(7, 8) == \
        [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
    assert m.make_empty_board(7, 9) == \
        [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

def test_make_random_board():
    for _ in range(NTESTS_LIFE):
        nrows = random.randint(4, 7)
        ncols = nrows + random.randint(-2, 2)
        p = random.random()
        b = m.make_random_board(nrows, ncols, p)
        assert type(b) is list  # check that b is a list
        assert len(b) == nrows
        for r in range(nrows):
            assert type(b[r]) is list
            assert len(b[r]) == ncols
        for r in range(nrows):
            for c in range(ncols):
                assert b[r][c] == 0 or b[r][c] == 1

        # Make a new board. All values should be 1.
        b = m.make_random_board(nrows, ncols, 1.0)
        for r in range(nrows):
            for c in range(ncols):
                assert b[r][c] == 1

        # Make a new board.  All values should be 0.
        b = m.make_random_board(nrows, ncols, 0.0)
        for r in range(nrows):
            for c in range(ncols):
                assert b[r][c] == 0

def test_display_board():
    for _ in range(NTESTS_LIFE):
        nrows = random.randint(4, 7)
        ncols = nrows + random.randint(-2, 2)
        p = random.random()
        b = m.make_random_board(nrows, ncols, p)
        s = m.display_board(b)
        assert type(s) is str
        for char in s:
            assert char in [' ', '*', '+', '-', '|', '\n']
        lines = s.split('\n')  # break on newlines
        assert len(lines) == nrows + 3
        assert lines[-1] == ''  # last line was the extra newline at the end
        lines.pop()  # get rid of the last line
        first = lines.pop(0)  # first line; part of the surrounding box
        last  = lines.pop()   # last line; part of the surrounding box
        first = first.rstrip()  # in case there are trailing blanks
        last = last.rstrip()  # in case there are trailing blanks
        assert len(first) == ncols + 2
        assert first[0] == '+' and first[-1] == '+'
        for i in range(1, ncols + 1):
            assert first[i] == '-'
        assert len(last) == ncols + 2
        assert last[0] == '+' and last[-1] == '+'
        for i in range(1, ncols + 1):
            assert last[i] == '-'
        for line in lines:
            line = line.rstrip()
            assert len(line) == ncols + 2
            assert line[0] == '|'
            assert line[-1] == '|'
            for char in line[1:-1]:
                assert char in [' ', '*']

def test_display_board_2():
    assert m.display_board([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]) == \
        '+----+\n|    |\n|    |\n|    |\n|    |\n+----+\n'
    assert m.display_board([[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]) == \
        '+------+\n|      |\n|      |\n|*     |\n|      |\n+------+\n'
    assert m.display_board([[1, 0, 1, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 0, 0, 1, 0, 1], [0, 1, 1, 1, 1, 0]]) == \
        '+------+\n|* * * |\n|  * * |\n|   * *|\n| **** |\n+------+\n'
    assert m.display_board([[1, 1, 0, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 0]]) == \
        '+----+\n|** *|\n|****|\n|****|\n| ***|\n| ** |\n+----+\n'
    assert m.display_board([[1, 1, 1, 1], [1, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]) == \
        '+----+\n|****|\n|*** |\n|****|\n|****|\n|****|\n+----+\n'
    assert m.display_board([[0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0], [0, 1, 1, 0, 0, 1], [1, 0, 1, 1, 0, 1]]) == \
        '+------+\n|    * |\n| *  **|\n| *    |\n| **  *|\n|* ** *|\n+------+\n'
    assert m.display_board([[1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 0, 0], [1, 0, 1, 1, 0, 1]]) == \
        '+------+\n|***** |\n|******|\n|*** **|\n|****  |\n|* ** *|\n+------+\n'
    assert m.display_board([[0, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 0, 1], [1, 1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]]) == \
        '+-------+\n| ******|\n|*******|\n|***** *|\n|** ****|\n|*******|\n+-------+\n'
    assert m.display_board([[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 0, 1]]) == \
        '+-------+\n|*******|\n|****** |\n|*******|\n|*******|\n|***** *|\n+-------+\n'
    assert m.display_board([[1, 1, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 1, 1]]) == \
        '+----+\n|** *|\n| ***|\n|****|\n| ** |\n|* **|\n|****|\n+----+\n'
    assert m.display_board([[0, 0, 0, 0, 1, 0], [1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0]]) == \
        '+------+\n|    * |\n|* *   |\n|      |\n|      |\n| * * *|\n|      |\n+------+\n'
    assert m.display_board([[1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 0, 1, 0, 1, 0], [0, 0, 1, 0, 0, 1], [1, 0, 0, 0, 1, 0]]) == \
        '+------+\n|*     |\n|*     |\n|*  * *|\n|  * * |\n|  *  *|\n|*   * |\n+------+\n'
    assert m.display_board([[0, 1, 0, 1, 0, 0], [1, 1, 1, 0, 1, 0], [1, 0, 0, 1, 0, 0], [0, 0, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1], [1, 1, 0, 1, 0, 0]]) == \
        '+------+\n| * *  |\n|*** * |\n|*  *  |\n|  ****|\n| * * *|\n|** *  |\n+------+\n'
    assert m.display_board([[1, 0, 0, 0, 0, 1, 1], [1, 1, 1, 0, 1, 1, 0], [0, 1, 0, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0]]) == \
        '+-------+\n|*    **|\n|*** ** |\n| * ****|\n|  *****|\n|    ** |\n|***    |\n+-------+\n'
    assert m.display_board([[0, 1, 1, 1, 0, 0, 1], [0, 1, 1, 1, 1, 0, 1], [1, 0, 0, 0, 1, 1, 1], [1, 0, 1, 1, 1, 1, 0], [1, 1, 1, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0, 0]]) == \
        '+-------+\n| ***  *|\n| **** *|\n|*   ***|\n|* **** |\n|***  **|\n|* * *  |\n+-------+\n'
    assert m.display_board([[0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0]]) == \
        '+--------+\n|   *    |\n|  *     |\n| *****  |\n|     *  |\n|  **    |\n|   * *  |\n+--------+\n'
    assert m.display_board([[1, 1, 0, 1, 1, 0, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]]) == \
        '+--------+\n|** ** **|\n|********|\n|********|\n|******* |\n|* ******|\n|********|\n+--------+\n'
    assert m.display_board([[1, 0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 1, 0, 1], [0, 1, 0, 1, 0, 0, 0], [1, 0, 0, 0, 0, 1, 1], [1, 0, 0, 0, 1, 1, 1], [1, 0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 1, 0, 1]]) == \
        '+-------+\n|* *    |\n| *  * *|\n| * *   |\n|*    **|\n|*   ***|\n|*  *   |\n|*  ** *|\n+-------+\n'
    assert m.display_board([[1, 1, 1, 1, 0, 1, 1], [0, 0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1, 1]]) == \
        '+-------+\n|**** **|\n|  *****|\n|*******|\n|*******|\n|* *****|\n|*******|\n|** ****|\n+-------+\n'
    assert m.display_board([[0, 0, 0, 0, 0, 0, 1, 0], [1, 0, 1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 1, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0]]) == \
        '+--------+\n|      * |\n|* *   * |\n|*      *|\n|*  **   |\n|  *   * |\n|*   *   |\n|    *   |\n+--------+\n'

def test_board_sums():
    for _ in range(NTESTS_LIFE):
        nrows = random.randint(4, 7)
        ncols = nrows + random.randint(-2, 2)
        p = random.random()
        b = m.make_random_board(nrows, ncols, p)
        b2 = copy.deepcopy(b)
        sums = m.board_sums(b)
        assert type(sums) is list
        assert len(sums) == nrows
        for r in range(len(b)):
            assert type(sums[r]) is list
            assert len(sums[r]) == ncols
        for r in range(len(sums)):
            row = sums[r]
            for c in range(len(row)):
                val = row[c]
                assert type(val) is int
                assert val >= 0 and val <= 8
        # Make sure the input board is unchanged.
        assert b == b2

        # Make a new board.
        # Fill the board with 1s; sums should all be 8.
        b = m.make_random_board(nrows, ncols, 1.0)
        sums = m.board_sums(b)
        for r in range(nrows):
            for c in range(ncols):
                assert sums[r][c] == 8

        # Make a new board.
        # Fill the board with 0s; sums should all be 0.
        b = m.make_random_board(nrows, ncols, 0.0)
        sums = m.board_sums(b)
        for r in range(nrows):
            for c in range(ncols):
                assert sums[r][c] == 0

def test_board_sums_2():
    assert m.board_sums([[1, 0], [0, 1], [0, 0], [0, 1]]) == \
        [[4, 4], [3, 2], [4, 2], [3, 2]]
    assert m.board_sums([[0, 0, 0], [0, 1, 1], [0, 0, 0], [0, 0, 0]]) == \
        [[2, 2, 2], [2, 1, 1], [2, 2, 2], [0, 0, 0]]
    assert m.board_sums([[0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0]]) == \
        [[1, 0, 0, 1, 1], [2, 1, 1, 1, 0], [2, 0, 1, 1, 1], [1, 1, 1, 0, 0]]
    assert m.board_sums([[1, 1, 1, 1, 0], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 0, 1, 1]]) == \
        [[7, 7, 7, 6, 8], [7, 8, 8, 7, 7], [8, 7, 7, 7, 8], [7, 7, 8, 6, 7]]
    assert m.board_sums([[1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 1, 1], [1, 0, 0, 1, 1, 1]]) == \
        [[6, 6, 3, 6, 6, 8], [7, 7, 5, 7, 6, 8], [7, 6, 5, 6, 7, 8], [6, 6, 5, 6, 7, 8]]
    assert m.board_sums([[0, 0, 0], [0, 1, 1], [0, 0, 0], [1, 0, 1], [0, 0, 1]]) == \
        [[3, 3, 3], [2, 1, 1], [4, 4, 4], [2, 3, 2], [3, 3, 2]]
    assert m.board_sums([[1, 1, 1, 1], [1, 1, 1, 1], [0, 1, 0, 1], [1, 0, 1, 1], [1, 1, 1, 1]]) == \
        [[8, 8, 8, 8], [7, 6, 7, 6], [7, 5, 7, 6], [6, 6, 6, 6], [7, 7, 7, 8]]
    assert m.board_sums([[1, 1, 1, 1], [1, 0, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]) == \
        [[7, 7, 7, 8], [6, 7, 7, 7], [7, 6, 7, 7], [7, 7, 8, 7], [8, 8, 8, 8]]
    assert m.board_sums([[1, 0, 1, 1, 1], [1, 0, 1, 0, 0], [0, 0, 0, 1, 1], [1, 1, 0, 0, 0], [1, 1, 0, 0, 0]]) == \
        [[4, 6, 3, 3, 4], [3, 4, 3, 6, 6], [4, 4, 3, 2, 3], [4, 3, 3, 2, 4], [5, 5, 4, 3, 5]]
    assert m.board_sums([[1, 0, 0, 1, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0]]) == \
        [[1, 2, 2, 0, 2], [2, 2, 3, 2, 2], [1, 2, 1, 1, 0], [1, 2, 1, 1, 1], [0, 1, 0, 0, 1], [2, 2, 1, 1, 3]]
    assert m.board_sums([[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1]]) == \
        [[1, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 1, 1], [2, 0, 0, 0, 2, 1], [2, 0, 0, 0, 2, 1]]
    assert m.board_sums([[0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0]]) == \
        [[1, 1, 2, 2, 1, 1], [2, 2, 2, 0, 0, 0], [2, 1, 2, 0, 0, 0], [3, 2, 2, 0, 0, 1], [1, 3, 2, 2, 1, 2], [2, 3, 1, 2, 0, 2]]
    assert m.board_sums([[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]]) == \
        [[8, 8, 8, 8, 8, 8, 8], [8, 8, 8, 8, 8, 8, 8], [8, 8, 8, 8, 8, 8, 8], [8, 8, 8, 8, 8, 8, 8], [8, 8, 8, 8, 8, 8, 8], [8, 8, 8, 8, 8, 8, 8]]
    assert m.board_sums([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == \
        [[8, 8, 8, 8, 8], [8, 8, 8, 8, 8], [8, 8, 8, 8, 8], [8, 8, 8, 8, 8], [8, 8, 8, 8, 8], [8, 8, 8, 8, 8], [8, 8, 8, 8, 8]]
    assert m.board_sums([[1, 1, 1, 1, 1, 0], [0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 1], [1, 0, 0, 1, 1, 0], [1, 0, 1, 1, 0, 0], [0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 0, 1]]) == \
        [[4, 5, 6, 6, 5, 5], [6, 6, 5, 5, 5, 5], [4, 3, 4, 5, 6, 5], [4, 5, 4, 3, 3, 5], [2, 4, 3, 4, 4, 4], [4, 5, 4, 4, 3, 2], [5, 5, 5, 5, 4, 3]]
    assert m.board_sums([[0, 0, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0, 0]]) == \
        [[3, 2, 2, 2, 1, 2, 1], [3, 1, 1, 1, 1, 2, 2], [2, 4, 2, 1, 0, 0, 2], [2, 3, 0, 1, 0, 1, 3], [2, 2, 1, 1, 0, 1, 1], [2, 1, 1, 1, 1, 1, 2], [1, 1, 1, 1, 2, 2, 2]]
    assert m.board_sums([[0, 1, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0]]) == \
        [[1, 0, 2, 2, 2, 1, 1], [1, 1, 1, 1, 2, 2, 1], [1, 1, 1, 0, 0, 0, 0], [2, 1, 2, 0, 0, 0, 0], [3, 3, 3, 2, 1, 1, 1], [1, 3, 2, 3, 1, 1, 1], [2, 3, 3, 3, 4, 3, 2]]
    assert m.board_sums([[1, 1, 0, 0, 1, 1, 0], [1, 0, 0, 0, 0, 0, 1], [1, 1, 0, 1, 0, 0, 1], [1, 1, 0, 0, 0, 0, 1], [0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1], [0, 0, 1, 0, 1, 0, 1]]) == \
        [[4, 3, 2, 3, 2, 4, 5], [6, 5, 3, 2, 3, 4, 5], [7, 4, 3, 0, 1, 3, 5], [6, 4, 4, 2, 2, 3, 3], [5, 2, 2, 1, 0, 3, 3], [3, 2, 2, 3, 2, 4, 1], [4, 3, 1, 3, 2, 5, 3]]
    assert m.board_sums([[0, 0, 0, 1, 1, 0, 1], [1, 1, 0, 1, 0, 1, 1], [1, 1, 1, 1, 0, 1, 1], [1, 1, 0, 1, 1, 0, 0], [1, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1, 1]]) == \
        [[7, 5, 6, 5, 6, 7, 6], [6, 4, 6, 4, 6, 5, 6], [7, 6, 6, 4, 6, 4, 6], [7, 7, 8, 5, 5, 5, 7], [6, 7, 7, 5, 6, 3, 5], [7, 8, 8, 6, 7, 5, 8], [5, 5, 6, 6, 6, 5, 5]]
    assert m.board_sums([[0, 1, 1, 1, 0, 1, 1, 1], [1, 1, 1, 1, 0, 1, 0, 1], [0, 0, 0, 1, 1, 1, 0, 1], [0, 0, 0, 1, 1, 0, 1, 0], [1, 0, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 0, 0, 1, 1, 0, 0]]) == \
        [[7, 6, 6, 4, 6, 4, 5, 4], [5, 4, 6, 5, 7, 4, 7, 4], [4, 3, 5, 5, 6, 4, 5, 3], [3, 1, 3, 4, 6, 5, 4, 4], [3, 4, 5, 5, 7, 4, 4, 3], [5, 5, 4, 4, 6, 4, 4, 4], [5, 6, 7, 6, 6, 5, 5, 4]]

def test_display_board_sums():
    for _ in range(NTESTS_LIFE):
        nrows = random.randint(4, 7)
        ncols = nrows + random.randint(-2, 2)
        p = random.random()
        b = m.make_random_board(nrows, ncols, p)
        s = m.display_board_sums(b)
        assert type(s) is str
        for char in s:
            assert char in '012345678+-|\n'
        lines = s.split('\n')  # break on newlines
        assert len(lines) == nrows + 3
        assert lines[-1] == ''  # last line was the extra newline at the end
        lines.pop()  # get rid of the last line
        first = lines.pop(0)  # first line; part of the surrounding box
        last  = lines.pop()   # last line; part of the surrounding box
        first = first.rstrip()  # in case there are trailing blanks
        last = last.rstrip()  # in case there are trailing blanks
        assert len(first) == ncols + 2
        assert first[0] == '+' and first[-1] == '+'
        for i in range(1, ncols + 1):
            assert first[i] == '-'
        assert len(last) == ncols + 2
        assert last[0] == '+' and last[-1] == '+'
        for i in range(1, ncols + 1):
            assert last[i] == '-'
        for line in lines:
            line = line.rstrip()
            assert len(line) == ncols + 2
            assert line[0] == '|'
            assert line[-1] == '|'
            for char in line[1:-1]:
                assert char in '012345678'

def test_display_board_sums_2():
    assert m.display_board_sums([[0, 0], [0, 0], [0, 0], [1, 0]]) == \
        '+--+\n|12|\n|00|\n|12|\n|02|\n+--+\n'
    assert m.display_board_sums([[1, 1], [1, 1], [1, 0], [0, 0]]) == \
        '+--+\n|55|\n|67|\n|35|\n|45|\n+--+\n'
    assert m.display_board_sums([[0, 0, 1], [1, 0, 1], [0, 1, 1], [1, 1, 1]]) == \
        '+---+\n|665|\n|454|\n|766|\n|555|\n+---+\n'
    assert m.display_board_sums([[0, 0, 0], [1, 1, 0], [1, 0, 0], [0, 1, 0], [1, 0, 0]]) == \
        '+---+\n|333|\n|223|\n|344|\n|323|\n|122|\n+---+\n'
    assert m.display_board_sums([[0, 0, 0, 1], [0, 1, 0, 0], [1, 0, 0, 1], [0, 0, 1, 0], [0, 0, 0, 0]]) == \
        '+----+\n|2120|\n|4133|\n|2332|\n|2213|\n|1122|\n+----+\n'
    assert m.display_board_sums([[1, 1, 0, 0], [1, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1]]) == \
        '+----+\n|6655|\n|5655|\n|6666|\n|6666|\n|6555|\n+----+\n'
    assert m.display_board_sums([[0, 0, 0, 0, 0], [0, 0, 1, 0, 1], [0, 1, 0, 0, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 1]]) == \
        '+-----+\n|32133|\n|32131|\n|31231|\n|42123|\n|11011|\n+-----+\n'
    assert m.display_board_sums([[1, 0, 0, 1, 1], [0, 1, 1, 0, 0], [1, 0, 1, 1, 0], [1, 1, 1, 0, 1], [0, 1, 0, 0, 0]]) == \
        '+-----+\n|34422|\n|44455|\n|47544|\n|45443|\n|64445|\n+-----+\n'
    assert m.display_board_sums([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == \
        '+-----+\n|88888|\n|88888|\n|77887|\n|87887|\n|77887|\n+-----+\n'
    assert m.display_board_sums([[0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 1]]) == \
        '+------+\n|101021|\n|001110|\n|100122|\n|200122|\n|201242|\n+------+\n'
    assert m.display_board_sums([[1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [1, 0, 1, 1, 1, 0], [1, 1, 0, 1, 1, 1]]) == \
        '+------+\n|876778|\n|777777|\n|667876|\n|566777|\n|666667|\n+------+\n'
    assert m.display_board_sums([[1, 1, 1, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1]]) == \
        '+-------+\n|6678887|\n|7878888|\n|7778888|\n|7788887|\n|8788887|\n+-------+\n'
    assert m.display_board_sums([[1, 0, 1, 1, 1], [1, 1, 1, 1, 0], [1, 0, 0, 1, 0], [0, 1, 1, 0, 1], [1, 0, 1, 1, 1], [0, 0, 0, 1, 1]]) == \
        '+-----+\n|45566|\n|45557|\n|46645|\n|54465|\n|44465|\n|54577|\n+-----+\n'
    assert m.display_board_sums([[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]) == \
        '+------+\n|000000|\n|000000|\n|000000|\n|000000|\n|000000|\n|000000|\n+------+\n'
    assert m.display_board_sums([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1, 0]]) == \
        '+-------+\n|1110111|\n|0000000|\n|0000000|\n|0000000|\n|1110111|\n|1010101|\n+-------+\n'
    assert m.display_board_sums([[1, 1, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0, 1], [0, 1, 0, 0, 0, 0, 0]]) == \
        '+-------+\n|3232233|\n|4342533|\n|3031434|\n|3133442|\n|3121131|\n|4233332|\n+-------+\n'
    assert m.display_board_sums([[1, 1, 1, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == \
        '+-----+\n|88777|\n|88787|\n|88777|\n|88888|\n|88888|\n|88888|\n|88888|\n+-----+\n'
    assert m.display_board_sums([[1, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0]]) == \
        '+------+\n|011212|\n|121212|\n|120101|\n|022211|\n|222011|\n|103220|\n|222122|\n+------+\n'
    assert m.display_board_sums([[1, 1, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0, 1], [1, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 1, 0], [0, 0, 1, 0, 0, 0, 1]]) == \
        '+-------+\n|4443234|\n|5454433|\n|3232333|\n|2122221|\n|1124442|\n|1213122|\n|3546553|\n+-------+\n'
    assert m.display_board_sums([[1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1], [1, 0, 1, 1, 0, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 0, 1]]) == \
        '+-------+\n|7666676|\n|7566677|\n|6655777|\n|7777778|\n|8877677|\n|8878576|\n|8877576|\n+-------+\n'


def test_board_update():
    for _ in range(NTESTS_LIFE):
        nrows = random.randint(4, 7)
        ncols = nrows + random.randint(-2, 2)
        p = random.random()
        b = m.make_random_board(nrows, ncols, p)
        copy_b = copy.deepcopy(b)
        b2 = m.board_update(b)
        assert type(b2) is list
        assert len(b2) == nrows
        for r in range(len(b)):
            assert type(b2[r]) is list
            assert len(b2[r]) == ncols
        for r in range(nrows):
            for c in range(ncols):
                assert b[r][c] == 0 or b[r][c] == 1
        # Check that b wasn't modified when creating b2.
        assert b == copy_b

def test_board_update_2():
    assert m.board_update([[0, 1, 0], [0, 0, 0], [0, 0, 0], [0, 1, 0]]) == \
        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert m.board_update([[1, 0, 1], [1, 0, 1], [1, 1, 1], [1, 1, 1]]) == \
        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert m.board_update([[1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 1], [1, 1, 0, 1, 0]]) == \
        [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    assert m.board_update([[0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]) == \
        [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    assert m.board_update([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]) == \
        [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    assert m.board_update([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1]]) == \
        [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    assert m.board_update([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]) == \
        [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    assert m.board_update([[0, 0, 0, 0, 0], [0, 1, 0, 1, 1], [1, 0, 1, 0, 0], [1, 1, 1, 0, 0], [1, 1, 0, 0, 0]]) == \
        [[0, 1, 1, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 1], [1, 0, 1, 0, 0]]
    assert m.board_update([[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]) == \
        [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    assert m.board_update([[0, 0, 0, 1, 1, 1], [1, 0, 0, 0, 0, 1], [1, 0, 1, 0, 1, 1], [1, 1, 0, 1, 0, 0], [1, 1, 0, 1, 0, 0], [1, 1, 1, 1, 1, 1]]) == \
        [[0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    assert m.board_update([[1, 0, 0, 1, 1, 1], [0, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 0], [1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 1]]) == \
        [[1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0]]
    assert m.board_update([[1, 1, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 0, 1], [0, 0, 1, 1, 1, 0, 1], [1, 1, 0, 0, 1, 1, 1], [1, 1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]]) == \
        [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    assert m.board_update([[1, 0, 0, 0, 0], [1, 0, 0, 1, 0], [1, 1, 0, 0, 0], [0, 1, 0, 1, 1], [0, 0, 1, 1, 1], [1, 0, 0, 0, 0], [0, 1, 0, 0, 1]]) == \
        [[1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 1, 0, 0, 0], [0, 1, 1, 0, 0], [1, 1, 1, 0, 0], [0, 1, 0, 0, 1]]
    assert m.board_update([[0, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 1, 1, 1, 1], [1, 1, 1, 1, 0]]) == \
        [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    assert m.board_update([[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]) == \
        [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    assert m.board_update([[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]) == \
        [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    assert m.board_update([[0, 0, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1], [1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 1], [1, 1, 1, 1, 1, 1]]) == \
        [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    assert m.board_update([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 1], [0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]) == \
        [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    assert m.board_update([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0]]) == \
        [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    assert m.board_update([[1, 1, 1, 0, 1, 1, 1, 0], [1, 0, 0, 1, 1, 1, 1, 1], [0, 1, 1, 0, 0, 1, 1, 1], [1, 0, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 0, 0, 0], [1, 1, 1, 0, 1, 1, 0, 1]]) == \
        [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1]]

def test_board_to_num():
    for _ in range(NTESTS_LIFE):
        nrows = random.randint(4, 7)
        ncols = nrows + random.randint(-2, 2)
        p = random.random()
        b = m.make_random_board(nrows, ncols, p)
        n = m.board_to_num(b)
        assert type(n) is int
        assert n >= 0

def test_board_to_num_2():
    assert m.board_to_num([[0, 0], [0, 0], [1, 0], [0, 0]]) == \
        16
    assert m.board_to_num([[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]) == \
        4095
    assert m.board_to_num([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]) == \
        0
    assert m.board_to_num([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [0, 1, 0, 0]]) == \
        10756
    assert m.board_to_num([[0, 0, 0, 1], [1, 0, 0, 1], [0, 0, 0, 0], [1, 1, 0, 0]]) == \
        12440
    assert m.board_to_num([[0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1]]) == \
        589920
    assert m.board_to_num([[0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 1, 0, 1]]) == \
        10534944
    assert m.board_to_num([[1, 1, 0], [1, 0, 0], [1, 0, 1], [0, 1, 1], [1, 0, 1]]) == \
        23883
    assert m.board_to_num([[0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0]]) == \
        41024
    assert m.board_to_num([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 0], [1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 0, 1, 1, 0, 1]]) == \
        771741695
    assert m.board_to_num([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0, 0]]) == \
        3759183872
    assert m.board_to_num([[0, 0, 1, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1, 0], [1, 1, 0, 0, 1, 0, 1], [0, 0, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 1]]) == \
        17374171332
    assert m.board_to_num([[0, 0, 1, 0, 0, 1, 0], [1, 0, 0, 1, 1, 1, 1], [1, 0, 1, 1, 0, 0, 1], [1, 0, 0, 1, 1, 0, 1], [0, 1, 0, 1, 1, 0, 1]]) == \
        24347114660
    assert m.board_to_num([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]) == \
        524288
    assert m.board_to_num([[0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]) == \
        51539607554
    assert m.board_to_num([[1, 0, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 1, 1, 1]]) == \
        270475565432797
    assert m.board_to_num([[0, 0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 1, 1, 1]]) == \
        540945091100668
    assert m.board_to_num([[0, 1, 1, 0, 1, 0, 1], [1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]]) == \
        562949945032406
    assert m.board_to_num([[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]) == \
        0
    assert m.board_to_num([[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0]]) == \
        18014398509481984

if __name__ == '__main__':
    # Part 2.
    test_draw_tictactoe()
    test_rps()
    test_rpslk()
    # Uncomment this if you've done the Honor Roll problem:
    #test_rpslk2()
    test_poker_rank()

    # Part 3.
    test_make_empty_board()
    test_make_empty_board_2()

    test_make_random_board()

    test_display_board()
    test_display_board_2()

    test_board_sums()
    test_board_sums_2()

    test_display_board_sums()
    test_display_board_sums_2()

    test_board_update()
    test_board_update_2()

    test_board_to_num()
    test_board_to_num_2()

    print('All tests passed!')


