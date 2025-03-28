#gameboard.py
def print_board():
    print(board_key[0]+"/c/l"+board_key[1]+"/c/l"+board_key[2]+"/c/l")
    print(boardB)
    print(board1)
    print(boardB)
    print(boardD)
    print(boardB)
    print(board2)
    print(boardB)
    print(boardD)
    print(boardB)
    print(board3)
    print(boardB)

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
    win_rows=[row_123, row_456, row_789, row_147, row_258, row_369, row_159, row_357]

def buildboard():
    board_key=("1|2|3","-+-+-","4|5|6","-+-+-","7|8|9")
    boardB, board[1], board[2], board[3]=['_','_','_','|','_','_','_','|','_','_','_']
    boardD='-----------'
    box_pos=dict{"1":(1,1), "2":(5,1), "3":(9,1), "4":(1,2), "5":(5,2), "6":(9,2), "7":(1,3), "8":(5,3), "9":(9,3)}
    pos_box[1]=dict{"1":1, '5':2, '9':3, "1":4, '5':5, '9':6, "1":7, '5':8, '9':9"
    pos_box[2]=dict{"1":1, '5':2, '9':3, "1":4, '5':5, '9':6, "1":7, '5':8, '9':9}
    pos_box[3]=dict{"1":1, '5':2, '9':3, "1":4, '5':5, '9':6, "1":7, '5':8, '9':9}

