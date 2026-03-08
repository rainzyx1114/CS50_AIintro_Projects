"""
Tic Tac Toe Player
"""

import math
import copy

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
    """
    Returns player who has the next turn on a board.
    """
    num_X = 0
    num_O = 0
    for row in board:
        for chess in row:
            if (chess == X):
                num_X += 1
            elif (chess == O):
                num_O += 1
    if (num_X == num_O):
        return X
    else:
        return O
    
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i in range(3):
        for j in range(3):
            if (board[i][j] == EMPTY):
                actions.append((i, j))
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    change_board = copy.deepcopy(board)
    (i, j) = action
    if(change_board[i][j] != EMPTY):
        raise Exception("Invalid action!")
    else:
        change_board[i][j] = player(board)
    return change_board
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if (board[i][1] == board[i][2] and board[i][0] == board[i][1] and board[i][1] != EMPTY and board[i][0] != EMPTY and board[i][2] != EMPTY):
            return board[i][0]
    for j in range(3):
        if (board[0][j] == board[1][j] and board[0][j] == board[2][j] and board[1][j] != EMPTY and board[0][j] != EMPTY and board[2][j] != EMPTY):
            return board[0][j]
    if (board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[1][1] != EMPTY and board[0][0] != EMPTY and board[2][2] != EMPTY):
        return board[0][0]
    if (board[2][0] == board[1][1] and board[0][2] == board[1][1] and board[1][1] != EMPTY and board[2][0] != EMPTY and board[0][2] != EMPTY):
        return board[2][0]
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if(winner(board) != None):
        return True
    else:
        if(actions(board) != []):
            return False
        else:
            return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if(winner(board) == X):
        return 1
    elif(winner(board) == O):
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def min_value(board):
        if(terminal(board)):
            return utility(board)
        else:
            v = 99
            for action in actions(board):
                v = min(max_value(result(board, action)), v)
            return v
    def max_value(board):
        if(terminal(board)):
            return utility(board)
        else:
            v = -99
            for action in actions(board):
                v = max(min_value(result(board, action)), v)
            return v
    if(terminal(board)):
        return None
    else:
        if(player(board) == X):
            choice = ()
            v = -99
            for action in actions(board):
                if (min_value(result(board, action)) > v):
                    v = min_value(result(board, action))
                    choice = action
            return choice
        else:
            choice = ()
            v = 99
            for action in actions(board):
                if (max_value(result(board, action)) < v):
                    v = max_value(result(board, action))
                    choice = action
            return choice