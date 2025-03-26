#victory_test.py

#check horizontal rows: 123, 456, 789
#check vertical   rows: 147, 258, 369
#check diagonal   rows: 159, 357

def victory_test():
    #to start: win=false
    #each row is checked for 3 matching (X or O) entries
    #1 of 8 successful tests mean victory: win=true
    Xwin=false
    # horizontal
    row_123 = str(grid["cell[1]"]) + str(grid["cell[2]"]) + str(grid["cell[3]"]) 
    row_456 = str(grid["cell[4]"]) + str(grid["cell[5]"]) + str(grid["cell[6]"]) 
    row_789 = str(grid["cell[7]"]) + str(grid["cell[8]"]) + str(grid["cell[9]"]) 
    if (row_123 or row_456 or row789) == "XXX":
       Xwin = true
    # vertical
    row_147 = str(grid["cell[1]"]) + str(grid["cell[4]"]) + str(grid["cell[7]"]) 
       Xwin = true
    elif (grid["cell[2]"] == "X" and grid["cell[5]"] == "X" and grid["cell[8]"]== "X"): 
       Xwin = true
    elif (grid["cell[3]"] == "X" and grid["cell[6]"] == "X" and grid["cell[9]"]== "X"): 
       Xwin = true
    # diagonal
    elif (cell[1] == "X" and cell[5] == "X" and cell[9] == "X"): 
       Xwin = true
    elif (cell[3] == "X" and cell[5] == "X" and cell[7] == "X"):
       Xwin = true
    else:
       Xwin = false
    Owin=false
    # horizontal
    if (cell[1] == "O" and cell[2] == "O" and cell[3] == "O"): 
       Owin = true
    elif (cell[4] == "O" and cell[5] == "O" and cell[6] == "O"): 
       Owin = true
    elif (cell[7] == "O" and cell[8] == "O" and cell[9] == "O"): 
       Owin = true
    # vertical
    elif (cell[1] == "O" and cell[4] == "O" and cell[7] == "O"): 
       Owin = true
    elif (cell[2] == "O" and cell[5] == "O" and cell[8] == "O"): 
       Owin = true
    elif (cell[3] == "O" and cell[6] == "O" and cell[9] == "O"): 
       Owin = true
    # diagonal
    elif (cell[1] == "O" and cell[5] == "O" and cell[9] == "O"): 
       Owin = true
    elif (cell[3] == "O" and cell[5] == "O" and cell[7] == "O"):
       Owin = true
    else:
       Owin = false

    if Xwin:
       return "X"
    elif Owin:
       return "O"
    else:
       return "!"

# end of function.
