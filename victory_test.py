
def victory_test(grid):
    #victory_test.py

    #check horizontal rows: 123, 456, 789
    #check vertical   rows: 147, 258, 369
    #check diagonal   rows: 159, 357
    #to start: win=False
    #each row is checked for 3 matching (X or O) entries
    #1 of 8 successful tests mean victory: win=True
    Xwin = False
    # horizontal
    row_123 = str(grid["cell[1]"]) + str(grid["cell[2]"]) + str(grid["cell[3]"]) 
    row_456 = str(grid["cell[4]"]) + str(grid["cell[5]"]) + str(grid["cell[6]"]) 
    row_789 = str(grid["cell[7]"]) + str(grid["cell[8]"]) + str(grid["cell[9]"]) 
    if (row_123 or row_456 or row789) == "XXX":
       Xwin = True
       return "X"
    # vertical
    row_147 = str(grid["cell[1]"]) + str(grid["cell[4]"]) + str(grid["cell[7]"]) 
    row_258 = str(grid["cell[2]"]) + str(grid["cell[5]"]) + str(grid["cell[8]"]) 
    row_369 = str(grid["cell[3]"]) + str(grid["cell[6]"]) + str(grid["cell[9]"]) 
    if (row_147 or row_258 or row_369) == "XXX":
       Xwin = True
       return "X"
    # diagonal
    row_159 = str(grid["cell[1]"]) + str(grid["cell[5]"]) + str(grid["cell[9]"]) 
    row_369 = str(grid["cell[3]"]) + str(grid["cell[5]"]) + str(grid["cell[7]"]) 
    if (row_159 or row_357) == "XXX":
       Xwin = True
       return "X"
    Owin = False
    # horizontal
    row_123 = str(grid["cell[1]"]) + str(grid["cell[2]"]) + str(grid["cell[3]"]) 
    row_456 = str(grid["cell[4]"]) + str(grid["cell[5]"]) + str(grid["cell[6]"]) 
    row_789 = str(grid["cell[7]"]) + str(grid["cell[8]"]) + str(grid["cell[9]"]) 
    if (row_123 or row_456 or row789) == "OOO":
       Owin = True
       return "O"
    # vertical
    row_147 = str(grid["cell[1]"]) + str(grid["cell[4]"]) + str(grid["cell[7]"]) 
    row_258 = str(grid["cell[2]"]) + str(grid["cell[5]"]) + str(grid["cell[8]"]) 
    row_369 = str(grid["cell[3]"]) + str(grid["cell[6]"]) + str(grid["cell[9]"]) 
    if (row_147 or row_258 or row_369) == "OOO":
       Owin = True
       return "O"
    # diagonal
    row_159 = str(grid["cell[1]"]) + str(grid["cell[5]"]) + str(grid["cell[9]"]) 
    row_369 = str(grid["cell[3]"]) + str(grid["cell[5]"]) + str(grid["cell[7]"]) 
    if (row_159 or row_357) == "OOO":
       Owin = True
       return "O"

#    return "!"

