"""
Tic Tac Toe Player
"""

# from asyncio import FastChildWatcher
from cmath import inf
import math
import random

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
    x_count =0
    o_count = 0
    for row in board :
        for cell in row:
            if cell ==X:
                x_count +=1
            elif cell ==O:
                o_count +=1
    if x_count == o_count :
        return X
    elif x_count > o_count:
        return O

    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] ==None:
                actions.append([y,x])
    return actions
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    active_player = player(board)
    

    board[action[0]][action[1]] = active_player

    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # horizantal =False
    # diagnola = False 
    # vertical= False
    # y_checker = board[0][0]
    # for y in range(len(board)):
    #     x_checker = board[0][y]
    #     for x in range(len(board)):
    #         if board[x][y] == y_checker:
    #             vertical == True
    #         else :
    #             vertical == False 
    #             break

    #         if board[y][x] == x_checker:
    #             horizantal =True
    #         else:
    #             horizantal = False
    #             break
        
    #     if horizantal ==True:
    #         return x_checker

    #     if vertical == True :
    #         return y_checker
    if board[0][0] == board[0][1] and board[0][0] == board[0][2]:
        return board[0][0]
    
    if board[1][0] == board[1][1] and board[1][0] == board[1][2]:
        return board[1][0]
        
    if board[2][0] == board[2][1] and board[2][0] == board[2][2]:
        return board[2][0]
        
        
    if board[0][0] == board[1][0] and board[0][0] == board[2][0]:
        return board[0][0]     
    if board[0][1] == board[1][1] and board[0][1] == board[2][1]:
        return board[0][1]      
    if board[0][2] == board[1][2] and board[0][2] == board[2][2]:
        return board[0][2]  
        
    if board[0][0] == board [1][1] and board[0][0] == board[2][2]:
        return board[0][0]
    if board[0][2] == board [1][1] and board[2][0] == board[2][2]:
        return board[0][2]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True

    for row in board:
        for cell in row :
            if cell == EMPTY :
                return False
    return True



    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)

    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1 
    return 0

    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    min_action= []
    max_action = []
    def max_value(state):
        state_actions = actions(state)
        max_v = float('-inf')
        
        if terminal(state) :
            return utility(state)
        for action in state_actions:
            current_state = min_value(result(state,action))    
            if current_state > max_v :
                max_action.append(action)
            max_v = max(max_v,current_state)
        return max_v   

    def min_value(state):

        state_actions = actions(state)
        min_v = float('inf')
        if terminal(state) :
            return utility(state)
        for action in state_actions:    
            current_state = max_value(result(state,action))         
            if current_state < min_v :
                min_action.append(action)         
                print(min_action)  
            min_v = min(min_v,current_state) 
        return min_v
    
    
    if board == initial_state():
        state_actions = actions(board)
        return random.choice(state_actions)

    
    

    if player(board) == X :
        max_value(board)
        return (max_action[-1])
    if player(board) == O:
        min_value(board)
        return min_action[-1]
