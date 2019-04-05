'''
This program allows the user to interactively play the game of Sudoku.
'''

import sys

class SudokuError(Exception):
    pass

class SudokuLoadError(SudokuError):
    pass

class SudokuMoveError(SudokuError):
    pass

class SudokuCommandError(SudokuError):
    pass

class Sudoku:
    '''Interactively play the game of Sudoku.'''

    def __init__(self):
        board_in = []
        for x in range(0, 9):
            board_in2 = []
            for y in range (0, 9):
                board_in2.append(0)
            board_in.append(board_in2)
        self.board = board_in
        self.moves = []

    def load(self, filename):
        '''Loads the contents of the file into the object's board
        representation.'''
        file = open(filename, 'r')
        number_of_lines = sum(1 for line in file)
        print(number_of_lines)
        if number_of_lines != 9:
            raise SudokuLoadError('File needs nine lines.')
        x = 0
        for line in open(filename, 'r'):
            if len(line.strip()) != 9:
                raise SudokuLoadError('File lines each need to be nine\
characters long.')
            y = 0
            for char in line.strip():
                if char not in [str(z) for z in range(0,10)]:
                    raise SudokuLoadError('Acceptable characters are the number\
 digits.')
                self.board[x][y] = char
                y += 1
            x += 1
        file.close()
        self.moves = []
        

    def save(self, filename):
        '''Saves the object's board representation into a file.'''
        file = open(filename, 'w')
        for x in (0, len(self.board)):
            for y in (0, len(self.board[0])):
                file.write(str(self.board[x][y]))
            file.write('\n')
        file.close()

    def show(self):
        '''Pretty-print the current board representation.'''
        print()
        print('   1 2 3 4 5 6 7 8 9 ')
        for i in range(9):
            if i % 3 == 0:
                print('  +-----+-----+-----+')
            print(f'{i + 1} |', end='')
            for j in range(9):
                if self.board[i][j] == 0:
                    print(end=' ')
                else:
                    print(f'{self.board[i][j]}', end='')
                if j % 3 != 2 :
                    print(end=' ')
                else:
                    print('|', end='')
            print() 
        print('  +-----+-----+-----+')
        print()

    def move(self, row, col, val):
        '''Takes:
            row - an integer representing the row coordinate from 1 to 9
            col - an integer representing the column coordinate from 1 to 9
            val - an integer ranging from 1 to 9
            This method checks that the inputs are valid coordinates and that 
            the move is valid on this board. It makes the move by writing the
            value into the board representation. It appends the move into the
            list of moves stored in the object.'''
        check = list(range(1, 10))
        
        # check row and column
        if row not in check:
            raise SudokuMoveError('Row coordinate is invalid.')
        elif column not in check:
            raise SudokuMoveError('Column coordinate is invalid.')
            
        # check move
        if self.board[row - 1][col - 1] != 0:
            raise SudokuMoveError('Coordinates refer to occupied space.')
        for x in range (0, len(self.board[row - 1])):
            if self.board[row - 1][x] == val:
                raise SudokuMoveError('Row conflict.')
        for x in range (0, len(self.board)):
            if self.board[x][col - 1] == val:
                raise SudokuMoveError('Column conflict.')
        box_x = int(row - 1 / 3)
        box_y = int(col - 1 / 3)
        for x in range(box_x * 3, (box_x + 1) * 3):
            for y in range(box_y * 3, (box_y + 1) * 3):
                if self.board[x][y] == val:
                    raise SudokuMoveError('Box conflict.')
        self.board[row - 1][col - 1] = val
        self.moves.append((row, col, val))
            
    def undo(self):
        x = self.moves.pop()
        self.board[x[0] - 1][x[1] - 1] = 0

    def solve(self):
        while True:
            try:
                command = input('Input a command: ')
                if command == 'q':
                    break
                elif len(command) == 3:
                    for x in command:
                        try:
                            int(x)
                        except:
                            raise SudokuCommandError(command)
                    
                elif command == 'u':
                    self.undo()
                elif command[0] == 's':
                    self.save(command[2:])
            except Exception as e:
                print(str(e) + '\nTry again with a valid input.')
                
if __name__ == '__main__':
    s = Sudoku()

    while True:
        filename = input('Enter the sudoku filename: ')
        try:
            s.load(filename)
            break
        except FileNotFoundError as e:
            print(e)
        except SudokuLoadError as e:
            print(e)
    s.show()
    s.solve()

