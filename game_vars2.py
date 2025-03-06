# verticals: row_147, row_258, row_369
# horizontals: row_123, row_456, row_789
# diagonals: row_159, row_357

# for each verticle, horizontal, diagonal:
# build horizontal rows beginning with 1, 4, 7
row_123=row_456=row_789="0"
#row_456=row_456+board[2][1]+board[2][3]+board[2][5]
#row_789=row_789+board[3][1]+board[3][3]+board[3][5]

# build vertical row begtinning with 1, 2, 3
row_147=row_258=row_369="0"
#row_147=row_147+board[1][1]+board[2][1]+board[3][1]
#row_258+=board[1][3]+board[2][3]+board[3][3]
#row_369+=board[1][5]+board[2][5]+board[3][5]

# build diagonal rows biginning with 1, 3
row_159=row_357="0"
#row_159=row_159+board[1][1]+board[2][3]+board[3][5]
#row_357=row_357+board[1][5]+board[2][3]+board[3][1]

# put rows in an list so they can be interated easily
win_rows=[row_123, row_456, row_789, row_147, row_258, row_369, row_159, row_357]

win_x = 'XXX'
win_0 = 'OOO'
#board_key = ["1|2|3", "-+-+-", "4|5|6", "-+-+-", "7|8|9"]
#box_pos = {"1":(1,1), "2":(5,1), "3":(9,1), "4":(1,2), "5":(5,2), "6":(9,2), "7":(1,3), "8":(5,3), "9":(9,3)}
#print(box_pos)
#pos_box[1]={"1":1, '5':2, '9':3, "1":4, '5':5, '9':6, "1":7, '5':8, '9':9}
#pos_box[2]={"1":1, '5':2, '9':3, "1":4, '5':5, '9':6, "1":7, '5':8, '9':9}
#pos_box[3]={"1":1, '5':2, '9':3, "1":4, '5':5, '9':6, "1":7, '5':8, '9':9}
win_list = ("789","456","123", "147", "258", "369","159", "357")
