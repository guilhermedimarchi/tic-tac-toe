"""
Tic Tac Toe Player
"""

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
    moves = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] is not EMPTY:
                moves += 1
    if moves % 2 == 0:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    act = []
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] is EMPTY:
                act.append((i, j))
    return act


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    (i, j) = action
    if i < 0 or i > 2 or j < 0 or j > 2:
        raise Exception
    r = copy.deepcopy(board)
    r[i][j] = player(board)
    return r


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # find out who made the winning move (previous move)
    winner_player = X
    if player(board) == X:
        winner_player = O

    diagonal = 0
    anti_diagonal = 0
    for i in range(0, 3):
        row = 0
        col = 0
        for j in range(0, 3):
            # check row
            if board[i][j] == winner_player:
                row += 1

            # check column
            if board[j][i] == winner_player:
                col += 1

            # check diagonal
            if i == j and board[i][j] == winner_player:
                diagonal += 1

            # check anti diagonal
            if (i+j) == 2 and board[i][j] == winner_player:
                anti_diagonal += 1

            # if winning player scored 3 in any it means he won
            if col == 3 or row == 3 or diagonal == 3 or anti_diagonal == 3:
                return winner_player
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or has_empty_spaces(board) is False:
        return True
    return False


def has_empty_spaces(board):
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == X:
        return 1
    elif w == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if X == player(board):
        return max_value(board)[1]
    return min_value(board)[1]


def max_value(board):
    """
    Returns max value and move that resulted in that value
    """
    if terminal(board):
        return utility(board), None
    v = -2
    move = None
    for action in actions(board):
        temp, act = min_value(result(board, action))
        if temp > v:
            v = temp
            move = action
    return v, move


def min_value(board):
    """
    Returns min value and move that resulted in that value
    """
    if terminal(board):
        return utility(board), None
    v = 2
    move = None
    for action in actions(board):
        temp, act = max_value(result(board, action))
        if temp < v:
            v = temp
            move = action
    return v, move





