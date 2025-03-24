# verticals: row_147, row_258, row_369
# horizontals: row_123, row_456, row_789
# diagonals: row_159, row_357

# for each verticle, horizontal, diagonal:
# build horizontal rows beginning with 1, 4, 7
row_123=row_456=row_789=["!","!","!","!"]

# build vertical row begtinning with 1, 2, 3
row_147=row_258=row_369=["!","!","!","!"]

# build diagonal rows biginning with 1, 3
row_159=row_357=["!","!","!","!"]

win_x = 'XXX'
win_0 = 'OOO'

#dictionary
grid={"cell[1]": "!","cell[2]": "!","cell[3]": "!","cell[4]": "!","cell[5]": "!","cell[6]": "!","cell[7]": "!","cell[8]": "!", "cell[9]": "!"}
def select_box(player):
    box = input("What box number do you want to put an " + player +"? ")
    # row_column = box_pos(str(box))
    grid["cell["+str(box)+"]"]= player
