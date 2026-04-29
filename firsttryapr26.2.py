#first try
import build_board
import game_vars
import select_player
print('Welcome to TicTacToe')
win_x='XXX'
win_0='OOO'
# player 1 selection of X or O
player1 = select_player.select_player()
print("player 1 will go first as " + player1)        

Board = build_board.build_board()
print (Board[0])
print (Board[1])
print (Board[2])
print (Board[3])
print (Board[4])

player = "X"
box_selected = game_vars.select_box(player)
#find selection in grid
