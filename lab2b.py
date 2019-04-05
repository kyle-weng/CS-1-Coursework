import random

#Ex. D.1:
def make_random_code():
    '''Returns a random four letter code. Each letter is one of the following:
        'R', 'G', 'B', 'Y', 'O', or 'W'.'''
    return_string = ''
    for i in range(0,4):
        return_string += random.choice(['R','G','B','Y','O','W'])
    return return_string

#Ex. D.2:
def count_exact_matches(str1, str2):
    '''Returns the number of times a character in the first string matches
    a character in the second string. It takes into account the relative location
    of the character.'''
    count = 0
    for i in range(4):
        if str1[i] == str2[i]:
            count += 1
    return count

#Ex. D.3:
def count_letter_matches(str1, str2):
    '''Returns the number of letters that are the same between the two input strings
    regardless of order.'''
    
    
    def unique_letters(str1):
        '''Given a string, return its unique letters-- that is, letters that are 
        repeated within the string are discounted.'''
        output = ''
        already_used = []
        for x in range(len(str1)):
            if str1[x] not in already_used:
                output += str1[x]
                already_used += list(str1[x])
        return output
    
    count = 0
    str1 = list(str1)
    str2 = list(str2)
    
    
    for x in unique_letters(str1):
        frequency_in_str1 = str1.count(x)
        frequency_in_str2 = str2.count(x)
        frequency_to_add = min(frequency_in_str1,frequency_in_str2)
        count += frequency_to_add
    return count

#Ex. D.4:
def compare_codes(code, guess):
    '''Takes two strings both of length 4. Compares them and outputs a string
    of identical length representing the evaluation of the guess according to 
    the game guidelines.'''
    black_pegs = count_exact_matches(code, guess) #frequency of black pegs
    white_pegs = count_letter_matches(code, guess) - black_pegs #frequency of white pegs
    dashes = abs(4 - (black_pegs + white_pegs)) #frequency of dashes
    blacks = 'b' * black_pegs
    whites = 'w' * white_pegs
    dashes = '-' * dashes
    output = blacks + whites + dashes
    return output

#Ex. D.5:
def run_game():
    '''Runs the game. Takes no arguments. Returns nothing.'''
    n = 0 #number of moves
    print('New game.')
    code = make_random_code()
    while True:
        guess = input('Enter your guess: ')
        print('Result: {}'.format(compare_codes(code, guess)))
        if compare_codes(code, guess) == 'bbbb':
            print('Congratulations! You cracked the code in {} moves!'.format(n))
            break

    