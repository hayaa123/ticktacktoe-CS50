import pytest 
from tictactoe import winner ,terminal, utility, minimax,result,player ,actions 
X="X"
O="O"

board1 = [["X"  ,"O"  ,"X"],
          [None ,"O"  ,"X"],
          ["O"  ,None ,"X"]]

board2 = [[X,O,X],
          [X,O,O],
          [O,X,X]]

board3 = [["X"  ,"O"  ,"X"  ],
          ["X"  ,"O"  ,None ],
          ["O"  ,None ,"X"  ]]

def test_board1_winner():
    actual = winner(board1)
    expected ="X"
    assert actual == expected
    
def test_board2_winner():
    actual = winner(board2)
    expected = None
    assert actual == expected
    
def test_board1_terminate():
    actual = terminal(board1)
    expected = True
    assert actual == expected
    
def test_board3_terminate():
    actual = terminal(board3)
    expected = False
    assert actual == expected 
    
def test_board1_utility():
    actual = utility(board1)
    expected = 1 
    assert actual == expected
    

def test_board3_player():
    actual= player(board3)
    expected = O
    assert actual == expected 

def test_board3_actions():
    actual = actions(board3)
    expected = [[1,2],[2,1]]
    assert actual == expected
    
# def test__board3_result():
#     actual = result(board3,[2,1])
#     expected = [["X"  ,"O"  ,"X"  ],
#                 ["X"  ,"O"  ,None ],
#                 ["O"  ,"O" ,"X"  ]]
    
#     print(actual)
    
#     assert actual ==expected

def test_board3_minmax():
    actual = minimax(board3)
    expected = [2,1]
    assert actual == expected    
