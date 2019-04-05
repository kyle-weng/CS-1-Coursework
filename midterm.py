# Name: Kyle Weng
# CMS cluster login name: kweng
# Midterm exam for Fall 2018 (solution set).
#

import random, sys, time

# ---------------------------------------------------------------------- 
# Part 1: Pitfalls.
# ---------------------------------------------------------------------- 

# Problem 1.1
# 1. The argument of the function is a string, but it's supposed to be a
#    variable.
# 2. The docstring should be enclosed within triple quotes, not single quotes.
# 3. On the sixth line of the function, there should be a colon at the end of
#    the "while" statement.
# 4. When checking for equality (line 9), there should be a == operator instead
#    of a = operator.
# 5. The indentation of Lines 12, 13, and 14 is one space short of the
#    indentation of the other lines in the function.

# Problem 1.2
# 1. The variable 'hist' is never defined in the ihist() function.
# 2. In lines 8-12 of ihist() (the "for" loop), n is a tuple. Therefore, n will
#    never be in hist, which means that line 10 (hist[n] == 1) will always be
#    run.
# 3. In line 10, checking if hist[n] is equal to 1 does nothing to actually
#    change anything in the hist variable (as opposed to replacing == with =,
#    which would actually change the value of hist[n]).
# 4. In lines 10 and 12, since n is a tuple, hist[n] will never evaluate
#    properly because the index of a list cannot be a tuple.
# 5. Line 15 won't run properly because "num, count" refers to two distinct
#    variables, not a single one.
# 6. The print statement at the end of the ihist() method doesn't use the
#    format() method after the string, so the string will literally print as
#    written.

# Problem 1.3
# 1. The docstring doesn't describe anything about the function.
# 2. There should be spaces before and after operators for readability.
# 3. The indentation spacing is inconsistent.
# 4. Variable names are not descriptive.
# 5. There should be a space after the # in the comment.
# 6. The comment is meaningless.

# ---------------------------------------------------------------------- 
# Part 2: Simple functions.
# ---------------------------------------------------------------------- 

#
# Problem 2.1
#

def draw_tictactoe(n):
    '''
    Takes a positive integer n, which represents the relative size of the board.
    Returns a string which, when printed, will draw a tic-tac-toe-like "board"
    onto the terminal.
    '''
    assert n > 0, "n must be positive."
    board = '\n'
    board += ((" " * n) + "|" + (" " * n) + "|" + (" " * n) + "\n") * n
    board += ("-") * n + "+" + ("-") * n + "+" + ("-") * n + "\n"
    board += ((" " * n) + "|" + (" " * n) + "|" + (" " * n) + "\n") * n
    board += ("-") * n + "+" + ("-") * n + "+" + ("-") * n + "\n"
    board += ((" " * n) + "|" + (" " * n) + "|" + (" " * n) + "\n") * n
    board += '\n'
    return board

def test_draw_tictactoe():
    print(draw_tictactoe(1))
    print(draw_tictactoe(2))
    print(draw_tictactoe(3))
    print(draw_tictactoe(4))
    print(draw_tictactoe(5))

#
# Problem 2.2
#

def rps(player1, player2):
    '''
    Takes two single characters corresponding to two players' choices, which can
    be "rock" ("R"), "paper" ("P"), or "scissors" ("S"). Returns whichever
    player wins (or a tie, if there is one).
    '''
    assert player1 == 'R' or 'P' or 'S', "Player 1 must use 'R', 'P', or 'S'."
    assert player2 == 'R' or 'P' or 'S', "Player 2 must use 'R', 'P', or 'S'."
    rps_defeats = {'R': 'S', 'P': 'R', 'S': 'P'}
    if rps_defeats[player1] == player2:
        return 1
    if rps_defeats[player2] == player1:
        return 2
    if rps_defeats[player1] != player2 and rps_defeats[player2] != player1:
        return 0
        

def rpslk(player1, player2):
    '''
    Takes two single characters corresponding to two players' choices, which can
    be "rock" ("R"), "paper" ("P"), "scissors" ("S"), "lizard" ("L"), or
    "Spock" ("K"). Returns whichever player wins (or a tie, if there is one).
    '''
    assert player1 == 'R' or 'P' or 'S' or 'L' or 'K', "Player 1 must use 'R',\
    'P', 'S', 'L', or 'K'."
    assert player2 == 'R' or 'P' or 'S' or 'L' or 'K', "Player 2 must use 'R',\
    'P', 'S', 'L', or 'K'."
    rps_defeats = {'R': 'SL', 'P': 'RK', 'S': 'PL', 'L': 'KP', 'K': 'SR'}
    if player2 in rps_defeats[player1]:
        return 1
    if player1 in rps_defeats[player2]:
        return 2
    if player2 not in rps_defeats[player1] and player1 not in rps_defeats\
    [player2]:
        return 0

#
# Problem 2.3
#

### Supplied to students.

ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
suits = ['S', 'H', 'D', 'C']

def validate_hand(hand):
    '''
    Validate a Poker hand.  If the hand is invalid, an assertion violation occurs.
    '''

    assert type(hand) is list
    assert len(hand) == 5
    for card in hand:
        assert type(card) is tuple
        assert len(card) == 2
        assert card[0] in ranks
        assert card[1] in suits

def random_hand():
    '''
    Return a randomly-generated Poker hand.

    Cards are represented as (rank, suit) tuples.
    Ranks are 2-10, or 'J', 'Q', 'K', 'A'
    Suits are one of 'S', 'H', 'D', 'C'
    '''

    # This uses a "list comprehension", which we haven't seen yet.
    deck = [(r, s) for r in ranks for s in suits]
    random.shuffle(deck)
    hand = deck[:5]
    # This uses "lambda", which we haven't seen yet.
    hand.sort(key=lambda c: ranks.index(c[0]))
    validate_hand(hand)
    return hand

def test_random_hand():
    '''
    Create a random hand, print it, and print its Poker rank.
    '''
    hand = random_hand()
    print(hand, poker_rank(hand))

def find_hand(p_rank):
    '''
    Print the first random hand that has a particular poker rank.
    Argument:
      p_rank: a poker rank
    '''
    count = 0
    while True:
        count += 1
        hand = random_hand()
        pr = poker_rank(hand)
        if pr == p_rank:
            print()
            break
        else:
            print('.', end='')
            sys.stdout.flush()
    print(hand, pr, count)

### End supplied to students.

# Helper functions for 'poker_rank' function go here.

def poker_rank(hand):
    '''
    Given a poker hand (a list of tuples of size two, each consisting of the
    card rank and the suit), return a two character string representing the
    ranking of the poker hand.
    '''
    precedence = ['SF', '4K', 'FH', 'FL', 'ST', '3K', '2P', '1P', 'NP']
    
    def convert_to_histogram(hand, choice):
        '''Generates a dictionary histogram with ranks or suits as keys and
        frequency of the ranks or suits as values. Takes the poker hand and an
        integer representing the choice (0 for ranks, 1 for suits) for which
        the function will count the frequency of.'''
        return_dictionary = {}
        for x in range (0, len(hand), 1):
            return_dictionary[hand[x][choice]] = 0
        for x in range (0, len(hand), 1):
            return_dictionary[hand[x][choice]] += 1
        return return_dictionary

    def check_straight(hand):
        histogram = list(convert_to_histogram(hand, 0).keys())
        new_histogram = []
        new_histogram_special_case = [] #because ace can either be "1" or "14"
        for x in range (0, len(histogram), 1):
            if histogram[x] == 'J':
                new_histogram.append(11)
                new_histogram_special_case.append(11)
            elif histogram[x] == 'Q':
                new_histogram.append(12)
                new_histogram_special_case.append(12)
            elif histogram[x] == 'K':
                new_histogram.append(13)
                new_histogram_special_case.append(13)
            elif histogram[x] == 'A':
                new_histogram.append(1)
                new_histogram_special_case.append(14)
            else:
                new_histogram.append(histogram[x])
                new_histogram_special_case.append(histogram[x])
        if ((len(new_histogram) == 5) and (max(new_histogram) -\
            min(new_histogram) + 1 == 5)) or (len(new_histogram_special_case)==\
            5 and (max(new_histogram_special_case) -\
            min(new_histogram_special_case) + 1 == 5)):
            return 'ST'
        else:
            return 'NP'
    
    def check_flush(hand):
        if 5 in list(convert_to_histogram(hand, 1).values()):
            return 'FL'
        else:
            return 'NP'
    
    def check_straight_flush(hand):
        if check_straight(hand) == 'ST' and check_flush(hand) == 'FL':
            return 'SF'
        else:
            return 'NP'
        
    def check_n_of_a_kind(hand):
        if 4 in list(convert_to_histogram(hand, 0).values()):
            return '4K'
        elif 3 in list(convert_to_histogram(hand, 0).values()):
            return '3K'
        else:
            return 'NP'
        
    def check_full_house(hand):
        if 3 in list(convert_to_histogram(hand, 0).values()) and 2 in \
        list(convert_to_histogram(hand, 0).values()):
            return 'FH'
        else:
            return 'NP'
        
    def check_n_pairs(hand):
        if list(convert_to_histogram(hand, 0).values()).count(2) == 2:
            return '2P'
        elif list(convert_to_histogram(hand, 0).values()).count(2) == 1:
            return '1P'
        else:
            return 'NP'
    
    validate_hand(hand)
    results = [check_straight_flush(hand), check_n_of_a_kind(hand), \
               check_full_house(hand), check_flush(hand), check_straight(hand),\
               check_n_of_a_kind(hand), check_n_pairs(hand), \
               check_n_pairs(hand), check_n_pairs(hand)]
    for x in range (0, 9, 1):
        if precedence[x] == results[x]:
            return precedence[x]


# ---------------------------------------------------------------------- 
# Miniproject: Game of Life.
# ---------------------------------------------------------------------- 

def make_empty_board(nrows, ncols):
    '''
    Given a number of rows and a number of columns, returns an empty Life board
    with those dimensions.
    '''
    outer_list = []
    for x in range (0, nrows, 1):
        outer_list.append([0 for y in range(0,ncols)])
    return outer_list

def make_random_board(nrows, ncols, p):
    '''
    Returns a new board with dimensions nrows by ncolumns where each cell
    has been randomly set to 1 with probability p.
    '''
    
    def generate_inner_list(ncols, p):
        inner_list = []
        for x in range (0, ncols, 1):
            if random.random() < p:
                inner_list.append(1)
            else:
                inner_list.append(0)
        return inner_list
            
    outer_list = []
    for x in range (0, nrows, 1):
        outer_list.append(generate_inner_list(ncols, p))
    return outer_list

def display_board(board):
    '''
    Given a Life board, return a string that, when printed, displays the board.
    '''
    nrows = len(board)
    ncols = len(board[0])
    display_string = '+' + ncols * '-' + '+\n'
    for x in range (0, nrows, 1):
        display_addend = '|'
        for y in range (0, ncols, 1):
            if board[x][y] == 1:
                display_addend += '*'
            else:
                display_addend += ' '
        display_addend += '|\n'
        display_string += display_addend
    display_string += '+' + ncols * '-' + '+\n'
    return display_string

def board_sums(board):
    '''
    Takes a Life board and returns a new list of lists containing the neighbor
    sums.
    '''
    def wrap_around(n, dimension_length):
        if n < 0:
            return n + dimension_length
        elif n >= dimension_length:
            return n - dimension_length
        else:
            return n
    nrows = len(board)
    ncols = len(board[0])
    outer_list = []
    for x in range (0, nrows, 1):
        inner_list = []
        for y in range (0, ncols, 1):
            neighbor_indices = [(x - 1, y + 1), (x, y + 1), (x + 1, y + 1),\
                                (x - 1, y), (x + 1, y),\
                                (x - 1, y - 1), (x, y - 1), (x + 1, y - 1)]
            neighbor_sum = 0
            for index_tuple in neighbor_indices:
                neighbor_sum += board[wrap_around(index_tuple[0], nrows)]\
                [wrap_around(index_tuple[1], ncols)]
            inner_list.append(neighbor_sum)
        outer_list.append(inner_list)
    return outer_list

def display_board_sums(board):
    '''
    Takes a Life board and displays a board containing the original Life board's
    neighbor sums.
    '''
    neighbor_sums_board = board_sums(board)
    nrows = len(neighbor_sums_board)
    ncols = len(neighbor_sums_board[0])
    display_string = '+' + ncols * '-' + '+\n'
    for x in range (0, nrows, 1):
        display_addend = '|'
        for y in range (0, ncols, 1):
            display_addend += str(neighbor_sums_board[x][y])
        display_addend += '|\n'
        display_string += display_addend
    display_string += '+' + ncols * '-' + '+\n'
    return display_string

def board_update(board):
    '''
    Takes a Life board and computes the next version of the board via neighbor
    sums. Returns a printable string which will display the new state of the
    board.
    '''
    neighbor_sums_board = board_sums(board)
    nrows = len(board)
    ncols = len(board[0])
    outer_list = []
    for x in range (0, nrows, 1):
        inner_list = []
        for y in range (0, ncols, 1):
            neighbor_sum = neighbor_sums_board[x][y]
            if board[x][y] == 0 and neighbor_sum == 3:
                inner_list.append(1)
            elif board[x][y] == 1 and (neighbor_sum < 2 or neighbor_sum > 3):
                inner_list.append(0)
            else:
                inner_list.append(board[x][y])
        outer_list.append(inner_list)
    return outer_list

def board_to_num(board):
    '''
    Takes a Life board and computes and returns a single integer, which
    represents the board state compactly.
    '''
    nrows = len(board)
    ncols = len(board[0])
    board_state = 0
    multiplier = 1.0/2.0
    for x in range (0, nrows, 1):
        for y in range (0, ncols, 1):
            multiplier *= 2
            board_state += multiplier * board[x][y]
    return int(board_state)
            

### Supplied to students:

def interact(nrows, ncols, p):
    '''
    Print the board and update it interactively until the user doesn't want
    to continue any more.  The user presses <return> to print the next
    generation to the terminal and enters "." to end the simulation.

    Arguments:
      nrows: number of rows (an integer > 0)
      ncols: number of columns (an integer > 0)
      p: a float in the range [0.0, 1.0]

    Return value: nothing
    '''

    answer = ''

    b = make_random_board(nrows, ncols, p)
    while True:
        print(display_board(b))
        answer = input()
        if answer == ".":
            break
        b = board_update(b)

def run_to_end(nrows, ncols, p, delay = 0.1):
    '''
    Print the board and update it non-interactively until the display repeats an
    earlier configuration, at which point the simulation stops.

    Arguments:
      nrows: number of rows (an integer > 0)
      ncols: number of columns (an integer > 0)
      p: a float in the range [0.0, 1.0]
      delay: time delay between printing of generations, in seconds

    Return value: nothing
    '''

    answer = ''
    seen = {}

    b = make_random_board(nrows, ncols, p)
    while True:
        print(display_board(b))
        time.sleep(delay)
        b = board_update(b)
        n = board_to_num(b)
        if n in seen:
            break
        seen[n] = 1

### End supplied to students.

