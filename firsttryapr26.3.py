#first try
import build_board
import game_vars
import select_player
print('Welcome to TicTacToe')
win_x='XXX'
win_0='OOO'
# player 1 selection of X or O
player = select_player.select_player()
player1=player[0]
player2=player[1]
print("player 1 will go first as " + player1)        

Board = build_board.build_board()
print (Board[0])
print (Board[1])
print (Board[2])
print (Board[3])
print (Board[4])

box_selected = game_vars.select_box(player1)
print ("box selected is", box_selected)
#find selection in grid
