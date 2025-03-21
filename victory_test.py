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
    if (row_123[1] == "X" and row_123[2] == "X" and row_123[3] == "X"): 
       Xwin = true
    elif (row_456[1] == "X" and row_456[2] == "X" and row_456[3] == "X"): 
       Xwin = true
    elif (row_789[1] == "X" and row_789[2] == "X" and row_789[3] == "X"): 
       Xwin = true
    # vertical
    elif (row_147[1] == "X" and row_147[2] == "X" and row_147[3] == "X"): 
       Xwin = true
    elif (row_258[1] == "X" and row_258[2] == "X" and row_258[3] == "X"): 
       Xwin = true
    elif (row_369[1] == "X" and row_369[2] == "X" and row_369[3] == "X"): 
       Xwin = true
    # diagonal
    elif (row_159[1] == "X" and row_159[2] == "X" and row_159[3] == "X"): 
       Xwin = true
    elif (row_357[1] == "X" and row_357[2] == "X" and row_357[3] == "X"):
       Xwin = true
    else:
       Xwin = false
    Ywin=false
    # horizontal
    if (row_123[1] == "Y" and row_123[2] == "Y" and row_123[3] == "Y"): 
       Ywin = true
    elif (row_456[1] == "Y" and row_456[2] == "Y" and row_456[3] == "Y"): 
       Ywin = true
    elif (row_789[1] == "Y" and row_789[2] == "Y" and row_789[3] == "Y"): 
       Ywin = true
    # vertical
    elif (row_147[1] == "Y" and row_147[2] == "Y" and row_147[3] == "Y"): 
       Ywin = true
    elif (row_258[1] == "Y" and row_258[2] == "Y" and row_258[3] == "Y"): 
       Ywin = true
    elif (row_369[1] == "Y" and row_369[2] == "Y" and row_369[3] == "Y"): 
       Ywin = true
    # diagonal
    elif (row_159[1] == "Y" and row_159[2] == "Y" and row_159[3] == "Y"): 
       Ywin = true
    elif (row_357[1] == "Y" and row_357[2] == "Y" and row_357[3] == "Y"):
       Ywin = true
    else:
       Ywin = false

    if Xwin:
       return "X"
    if Ywin:
       return "O"

# end of function.
