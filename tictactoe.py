"""
Tic Tac Toe Player
"""

from copy import deepcopy
import math
from tkinter import Y


X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    # loops through board, counting the number of current moves and returning
    # the player who's turn it is
    x_count = 0
    o_count = 0

    for i in board:
        for j in i:
            if j == X:
                x_count+=1
            if j == O:
                o_count+=1

    if x_count==0 and o_count==0:
        return X
    elif x_count>o_count:
        return O
    elif o_count == x_count:
        return X
    else:
        return 'Over'
                


def actions(board):
    # loops through board checking if the space is taken
    # returns a set of the spaces which have not yet been used
    possible = set()
    for i, row in enumerate(board):
        for j, item in enumerate(row):
            if item == None:
                possible.add((i,j))
    if possible:    
        return possible
    return None



def result(board, action):
    # creates copy of given board
    # returns new board after making a legal move
    if terminal(board):
        return None

    kopy = deepcopy(board)
    turn  = player(board)
    if action in actions(board):
        kopy[action[0]][action[1]] = turn 
        return kopy

    raise Exception('Illegal move!')


def winner(board):
    # checks the two diagonal rows for matches
    if board[0][0] == X and board[1][1] == X and board[2][2]==X:
        return X
    if board[0][0] == O and board[1][1] == O and board[2][2]==O:
        return O
    
    if board[0][2] == X and board[1][1] == X and board[2][0]==X:
        return X
    if board[0][2] == O and board[1][1] == O and board[2][0]==O:
        return O

    # loops through board checking for vertical or horozontal matches
    for i in range(3):
        try:
            for j in range(3):
                if board[i][j] == X and board[i][j+1]==X and board[i][j+2]==X:
                    return X
                if board[i][j] == O and  board[i][j+1]==O and board[i][j+2]==O:
                    return O
                
                if board[i][j] == X and board[i+1][j]==X and board[i+2][j]==X:
                    return X
                if board[i][j] == O and board[i+1][j]==O and board[i+2][j]==O:
                    return O
        except IndexError:
            continue
        

# checks if game over
def terminal(board):
    # if game is over returns true
    if winner(board) != None:
        return True
    if actions(board) == None:
        return True
    
    return False

  

# returns numerical value for outcome of game
def utility(board):
    # x==1  O==-1  else==0
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0

# figurs out who's turn it is given a board, calls minimax 
# algorithm to determine which action to take
def minimax(board):
    if terminal(board):
        return None
    
    if player(board)==X:
        for action in actions(board):
            if max_value(board)== min_value(result(board,action)):
                return action
    
    if player(board)==O:
        for action in actions(board):
            if min_value(board)==max_value(result(board,action)):
                return action


# recursively loops through possible moves and figures out 
# the resulting utility

#
def max_value(board):
    if terminal(board):
        return utility(board)
    
    v=-2
    for action in actions(board):
        val_1 = min_value(result(board, action))
        if val_1 < v:
            continue
        v = max(v, val_1)
        # v cannot be greater than 1, so if it ==1, the move
        # is acceptable and v is returned
        # helps optimize the function
        if v==1:
            return v
    return v



def min_value(board):
    if terminal(board):
        return utility(board)

    v=2
    for action in actions(board):
        val_2 = max_value(result(board,action))
        if val_2 > v:
            continue
        v = min(v, val_2)
        if v==-1:
            return v
    return v




# def minimax(board):
#     if terminal(board):
#         return None

#     if player(board) == X:
#         for action in actions(board):
#             if min_value(result(board, action)) == max_value(board):
#                 return action 

#     if player(board) == O:
#         for action in actions(board):
#             if max_value(result(board, action)) == min_value(board):
#                 return action

    """
    Returns the optimal action for the current player on the board.
    """


# def max_value(board):
#     if terminal(board):
#         return utility(board)
#     v = -2
#     for action in actions(board):
#         v = max(v, min_value(result(board,action)))
#     return v

# def min_value(board):
#     if terminal(board):
#         return utility(board)
#     v = 2
#     for action in actions(board):
#         v = min(v, max_value(result(board, action)))
#     return v
