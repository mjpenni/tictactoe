#victory_test.py

#check horizontal rows: 123, 456, 789
#check vertical   rows: 147, 258, 369
#check diagonal   rows: 159, 357

#to start: win=false
#each row is checked for 3 matching (X or O) entries
#1 of 8 successful tests mean victory: win=true
Xwin=false
   # horizontal
if (row_123[1] == "X" and row_123[2] == "X" and row_123[3] == "X") or 
   (row_456[1] == "X" and row_456[2] == "X" and row_456[3] == "X") or 
   (row_789[1] == "X" and row_789[2] == "X" and row_789[3] == "X") or 
   # vertical
   (row_147[1] == "X" and row_147[2] == "X" and row_147[3] == "X") or 
   (row_258[1] == "X" and row_258[2] == "X" and row_258[3] == "X") or 
   (row_369[1] == "X" and row_369[2] == "X" and row_369[3] == "X") or 
   # diagonal
   (row_159[1] == "X" and row_159[2] == "X" and row_159[3] == "X") or 
   (row_357[1] == "X" and row_357[2] == "X" and row_357[3] == "X"):
   Xwin = true

Ywin=false
   # horizontal
if (row_123[1] and row_123[2] and row_123[3] == "Y") or
   (row_456[1] and row_456[2] and row_456[3] == "Y") or
   (row_789[1] and row_789[2] and row_789[3] == "Y") or
   # vertical
   (row_147[1] and row_147[2] and row_147[3] == "Y") or
   (row_258[1] and row_258[2] and row_258[3] == "Y") or
   (row_369[1] and row_369[2] and row_369[3] == "Y") or
   # diagonal
   (row_159[1] and row_159[2] and row_159[3] == "Y") or
   (row_357[1] and row_357[2] and row_357[3] == "Y"):
   Ywin=true

if Xwin:
   return(parameter="X")
if Ywin:
   return(parameter="O")
