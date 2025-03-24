#victory_test.py

#check horizontal rows: 123, 456, 789
#check vertical   rows: 147, 258, 369
#check diagonal   rows: 159, 357

#to start: win=false
#each row is checked for 3 matching (X or O) entries
#1 of 8 successful tests mean victory: win=true
def victory_test():
    Xwin=false
    # horizontal
    if (cell[1] == "X" and cell[2] == "X" and cell[3] == "X"): 
       Xwin = true
    elif (cell[4] == "X" and cell[5] == "X" and cell[6] == "X"): 
       Xwin = true
    elif (cell[7] == "X" and cell[8] == "X" and cell[9] == "X"): 
       Xwin = true
    # vertical
    elif (cell[1] == "X" and cell[4] == "X" and cell[7] == "X"): 
       Xwin = true
    elif (cell[2] == "X" and cell[5] == "X" and cell[8] == "X"): 
       Xwin = true
    elif (cell[3] == "X" and cell[6] == X" and cell[9] == "X"): 
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
    if Ywin:
       return "O"

# end of function.
