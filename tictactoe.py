#tictactoe.py
def var_def():
    pass

def print_board():
    print(vars.board_key[0]+"\r\n"+vars.board_key[1]+"\r\n"+vars.board_key[2]+"\r\n"+
          vars.board_key[3]+"\r\n"+vars.board_key[4]+"\r\n")
    #print(vars.boardB)
    print(vars.board[0])
    print(vars.board[1])
    # print(vars.boardB)
    #print(vars.boardD)
    #print(vars.boardB)
    print(vars.board[2])
    #print(vars.boardB)
    #print(vars.boardD)
    #print(vars.boardB)
    print(vars.board[3])
    #print(vars.boardB)

def select_box(player):
    vars.box = input("In what box number do you want to put an "+player+"? ")
    vars.row_column = vars.box_pos[str(vars.box)]
    print(vars.row_column) # debug
    vars.r0=vars.row_column[0]
    vars.r1=vars.row_column[1]
    #vars.board[vars.row_column[0]][vars.row_column[1]]=player
    vars.board[vars.r0,vars.r1]=player

def win_rows_build():
    # verticals: row_147, row_258, row_369
    # horizontals: row_123, row_456, row_789
    # diagonals: row_159, row_357

    # for each verticle, horizontal, diagonal:
    # build horizontal rows beginning with 1, 4, 7
    vars.row_123=vars.row_456=vars.row_789=0
    vars.row_123+=vars.board[1][1]+vars.board[1][5]+vars.board[1][9]
    vars.row_456+=vars.board[2][1]+vars.board[2][5]+vars.board[2][9]
    vars.row_789+=vars.board[3][1]+vars.board[3][5]+vars.board[3][9]

    # build vertical row begtinning with 1, 2, 3
    vars.row_147=vars.row_258=vars.row_369=0
    vars.row_147+=vars.board[1][1]+vars.board[2][1]+vars.board[3][1]
    vars.row_258+=vars.board[1][5]+vars.board[2][5]+vars.board[3][5]
    vars.row_369+=vars.board[1][9]+vars.board[2][9]+vars.board[3][9]

    # build diagonal rows biginning with 1, 3
    vars.row_159=vars.row_357=0
    vars.row_159+=vars.board[1][1]+vars.board[2][5]+vars.board[3][9]
    vars.row_357+=vars.board[1][9]+vars.board[2][5]+vars.board[3][1]

    # put rows in an list so they can be interated easily
    vars.win_rows=[vars.row_123, vars.row_456, vars.row_789, vars.row_147, vars.row_258, vars.row_369, vars.row_159, vars.row_357]

    def win_test():
        # test X's or O's for winning configuration
            for row in win_rows:
                if row == win_x:
                    print('X wins')
                    vars.restart_flag="Y"
                elif row == win_o:
                    print('O wins')
                    vars.restart_flag="Y"
                else:
                    print('Keep playing. No winner yet')
                    vars.restart_flag="N"

def char_pos(square):
    # lookup square (key) & return char_pos & row
    pass

def __main__():
    var_def()

#-----------------------------------------------------------------------------------
import tictactoe_vars as vars

if __name__ == "__main__":
    __main__()
print('Welcome to TicTacToe')
win_x = 'XXX'
win_0 = 'OOO'
board_key = ["1|2|3", "-+-+-", "4|5|6", "-+-+-", "7|8|9"]
board = [0,1,2,3]
#boardB = board[1] = board[2] = board[3] = "|___|___|___|"
board[1] = board[2] = board[3] = "|_|_|_|"
board[0]=",_____,"
#boardD = '-----------'
box_pos = {"1":(1,1), "2":(5,1), "3":(9,1), "4":(1,2), "5":(5,2), "6":(9,2), "7":(1,3), "8":(5,3), "9":(9,3)}
print(box_pos)
#pos_box[1]={"1":1, '5':2, '9':3, "1":4, '5':5, '9':6, "1":7, '5':8, '9':9}
#pos_box[2]={"1":1, '5':2, '9':3, "1":4, '5':5, '9':6, "1":7, '5':8, '9':9}
#pos_box[3]={"1":1, '5':2, '9':3, "1":4, '5':5, '9':6, "1":7, '5':8, '9':9}
win_list = ("789","456","123", "147", "258", "369","159", "357")
# player 1 selection of X or O
player1="N"
while player1 not in 'XO':
    player1=input('player 1: Do you want to be "X" or "O" ?')
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
go="S"
turns=0
while go not in "YNQ":
    go=input("Are you ready to play?  Y, N or Q: ")
    if go =='N' or go =='n':
        # enter again
        go = "N"
    elif go == 'Y' or go == 'y':
        # start game
        go="Y"
        print_board()
        turns += 1
        #print('got here')
        # player 1 make selection & after 3 check for win
        select_box(player1)
        # player 2 make selection & after 3 check for win
        select_box(player2)
        print('got here')
        select_box(player2)
        if turns>=3:
            #check for win
            win_rows_build()
            win_test()
    else:
        pass
#quit game
