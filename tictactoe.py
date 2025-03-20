#tictactoe.py

def select_box(player):
    box = input("What box number do you want to put an {player}?")
    row_column() = box_position(str(box))
    board[row_column(0),row_column(1)]=player

def char_pos(square):
    # lookup square (key) & return char_pos & row
    pass

#-------------------------------------------------------------------------------------
    
#main
import sim_print
import game_vars
from game_board.py import win_rows_build
import victory_test
player1="N"
while player1 not in 'XO':
    player1=input('player 1: Do you want to be "X" or "O" ?')
    if player1=="X":
        player2="O"
    elif player1=="O":
        player2="X"
    else:
        print("Please enter X or O.")

print("player 1 will go first")
go="S"
turns=0
while go not in "YNQ":
    go=input("Are you ready to play?  Y, N or Q: ")
    if go =='N':
        # enter again
        pass
    elif go == 'Y':
        # start game
        print_board
        turns += 1
        # player 1 make selection & after 3 check for win
        select_box(player1)
        # player 2 make selection & after 3 check for win
        select_box(player2)
        if turns>=3:
            #check for win
            win_rows_build()
            win_test()
    else:
        pass
        # small test change
        # quit game

