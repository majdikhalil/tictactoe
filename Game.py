import random
import sys


def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1 please select X OR O: ").upper()
        if marker == "X":
            return('X','O')
        if marker == "O":
            return('O','X')
def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9]== mark) or # checking across top 
    (board[4] == mark and board[5] == mark and board[6]== mark) or # checking across middle
    (board[1] == mark and board[2] == mark and board[3]== mark) or # checking across bottom
    (board[7] == mark and board[4] == mark and board[1]== mark) or # checking across left verticle 
    (board[9] == mark and board[6] == mark and board[3]== mark) or # checking across right verticle 
    (board[8] == mark and board[5] == mark and board[2]== mark) or # checking across middle verticle 
    (board[7] == mark and board[5] == mark and board[3]== mark) or # checking across diagonal
    (board[9] == mark and board[5] == mark and board[1]== mark))# checking across diagonal

def choose_first():
    randomnum = random.randint(0,1)
    if randomnum == 0:
        return ('Player 1')
    else:
        return ('Player 2')

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Where would you like to place next item ?: '))
    return position

def replay():
    return input('Do you want to play again? Yes Or No: ').lower().startswith('y')

