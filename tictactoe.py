#tictactoe.py

def char_pos(square):
 # lookup square (key) & return char_pos & row
    pass

#-------------------------------------------------------------------------------------
    
#main
from build_board import build_board
from display_board import display_board
from game_vars import select_box
#from game_vars import game_vars
from victory_test import victory_test

#dictionary
grid = {"cell[1]": "!","cell[2]": "!","cell[3]": "!","cell[4]": "!","cell[5]": "!","cell[6]": "!","cell[7]": "!","cell[8]": "!", "cell[9]": "!"}

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
        # for each verticle, horizontal, diagonal:
        # build horizontal rows beginning with 1, 4, 7
        row_123=row_456=row_789=["!","!","!","!"]
        # build vertical row beginning with 1, 2, 3
        row_147=row_258=row_369=["!","!","!","!"]
        # build diagonal rows biginning with 1, 3
        row_159=row_357=["!","!","!","!"]
        build_board()
        turns=0
        winner="!"
        while winner == "!":
            #print ("game start \n\n")
            #game_vars()
            turns += 1
            # player 1 make selection & after 3 check for win
            box=select_box(player1)
            grid["cell["+str(box)+"]"] = player1
            # player 2 make selection & after 3 check for win
            box=select_box(player2)
            grid["cell["+str(box)+"]"] = player2
            display_board(grid)
            print (turns)
            if turns >= 3:
                #check for a win
                winner = victory_test(grid)
        else:
            print (winner)
    elif go == "N":
        # repeat how?
        pass
    else:
        pass
        # small test change 
        # quit game
