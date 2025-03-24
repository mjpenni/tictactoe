#tictactoe.py 

def char_pos(square):
 # lookup square (key) & return char_pos & row
    pass

#-------------------------------------------------------------------------------------
    
#main
# import sim_print eh?
import build_board
import display_board
import game_vars
from game_vars import select_box

# from game_board.py import win_rows_build (defunct
import victory_test
go="S"
while go not in "YNQ":
    go = input("Are you ready to play?  Yy, Nn or Qq: ")
    go = go.upper()
    if go == 'Y':
        # start game
        player1="N"
        while player1 not in 'XO':
            player1=input('player 1: Do you want to be "X" or "O" ?')
            player1=player1.upper()
            if player1=="X":
                player2="O"
            elif player1=="O":
                player2="X"
            else:
                print("Please enter X or O.")
        print("player 1 will go first")
        turns=0
        display_board
        turns += 1
        # player 1 make selection & after 3 check for win
        select_box(player1)
        # player 2 make selection & after 3 check for win
        select_box(player2)
        if turns>=3:
            #check for win
            # win_rows_build() (defunct
            winner=victory_test()
    elif go == "N":
        # repeat how?
        pass
    else:
        pass
        # small test change
        # quit game

