#first try
import build_board
import game_vars
print('Welcome to TicTacToe')
win_x='XXX'
win_0='OOO'
# player 1 selection of X or O
player1="N"
while player1 not in 'XO':
    player1=input('player 1: Do you want to be X or O? ')
    if player1=="x":
        player1="X"
    elif player1=="o":
        player1="O"
    if player1=="X":
        player2="O"
    elif player1=="O":
        player2="X"
    else:
        print("Please enter X or O.")

print("player 1 will go first as " + player1)        

Board = build_board.build_board()
print (Board[0])
print (Board[1])
print (Board[2])
print (Board[3])
print (Board[4])

player = "X"
box_selected = game_vars.select_box(player)
print (box_selected)