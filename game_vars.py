def select_box(player):
    box = input("What box number do you want to put an " + player +"? ")
    return box
    # row_column = box_pos(str(box))
    grid["cell["+str(box)+"]"] = player
