#tictac2.py
def select_box(player):
    box = input("What box number do you want to put an {player}?")
    row_column() = box_position(str(box))
    board[row_column(0),row_column(1)]=player

def win_rows_build(): 
    # verticals: row_147, row_258, row_369 
    # horizontals: row_123, row_456, row_789
    # diagonals: row_159, row_357

    # for each verticle, horizontal, diagonal: 
    # build horizontal rows beginning with 1, 4, 7    
    row_123=row_456=row_789=0
    row_123+=board[1][1]+board[1][5]+board[1][9]
    row_456+=board[2][1]+board[2][5]+board[2][9] 
    row_789+=board[3][1]+board[3][5]+board[3][9] 
    
    # build vertical row begtinning with 1, 2, 3
    row_147=row_258=row_369=0
    row_147+=board[1][1]+board[2][1]+board[3][1]
    row_258+=board[1][5]+board[2][5]+board[3][5] 
    row_369+=board[1][9]+board[2][9]+board[3][9]  
    
    # build diagonal rows biginning with 1, 3
    row_159=row_357=0
    row_159+=board[1][1]+board[2][5]+board[3][9]
    row_357+=board[1][9]+board[2][5]+board[3][1]
    
    # put rows in an list so they can be interated easily
    win_rows[]=[row_123, row_456, row_789, row_147, row_258, row_369, row_159, row_357]

def win_test():        
    # test X's or O's for winning configuration
        for row in win_rows:
            if row == win_x:
                print ('X wins')`
                restart_flag="Y"`
            elif row == win_o:
                print ('O wins')
                restart_flag="Y"`
            else:
                print ('Keep playing. No winner yet')
                restart_flag="N"`
def char_pos(square):
    # lookup square (key) & return char_pos & row
    pass

#-------------------------------------------------------------------------------------
    
#main
from game_vars.py import #function file name (sans .py)
board_key=["1|2|3","-+-+-","4|5|6","-+-+-","7|8|9"]
boardB, board[1], board[2], board[3]=['_','_','_','|','_','_','_','|','_','_','_']
boardD='-----------'
box_pos=dict{"1":(1,1), "2":(5,1), "3":(9,1), "4":(1,2), "5":(5,2), "6":(9,2), "7":(1,3), "8":(5,3), "9":(9,3)}
pos_box[1]=dict{"1":1, '5':2, '9':3, "1":4, '5':5, '9':6, "1":7, '5':8, '9':9"
pos_box[2]=dict{"1":1, '5':2, '9':3, "1":4, '5':5, '9':6, "1":7, '5':8, '9':9}
pos_box[3]=dict{"1":1, '5':2, '9':3, "1":4, '5':5, '9':6, "1":7, '5':8, '9':9}

win_list=("789","456","123", "147", "258", "369","159", "357")
print('Welcome to TicTacToe')
win_x='XXX'
win_0='OOO'
# player 1 selection of X or O
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
        pass`
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
        # quit game

