#tictactoe.py 

def char_pos(square):
 # lookup square (key) & return char_pos & row
    pass

#-------------------------------------------------------------------------------------
    
#main
from build_board import build_board
from display_board import display_board
from game_vars import select_box
from game_vars import game_vars
from victory_test import victory_test
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
        grid = build_board()
        turns=0
        winner="!"
        while winner == "!":
            print ("game start \n\n")
            display_board(grid)
            game_vars.game_vars()
            turns += 1
            # player 1 make selection & after 3 check for win
            game_vars.select_box(player1)
            # player 2 make selection & after 3 check for win
            game_vars.select_box(player2)
            if turns >= 3:
                #check for a win
                winner = victory_test.victory_test()
        else:
            print (winner)
    elif go == "N":
        # repeat how?
        pass
    else:
        pass
        # small test change
        # quit game
