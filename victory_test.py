#victory_test.py

#check horizontal rows: 123, 456, 789
#check vertical   rows: 147, 258, 369
#check diagonal   rows: 159, 357

#to start: win=false
#each row is checked for 3 matching (X or O) entries
#1 of 8 successful tests mean victory: win=true
Xwin=false
   # horizontal
if (rows_123[1] and rows_123[2] and rows_123[3] == "X") or
   (rows_456[1] and rows_456[2] and rows_456[3] == "X") or
   (rows_789[1] and rows_789[2] and rows_789[3] == "X") or
   # vertical
   (rows_147[1] and rows_147[2] and rows_147[3] == "X") or
   (rows_258[1] and rows_258[2] and rows_258[3] == "X") or
   (rows_369[1] and rows_369[2] and rows_369[3] == "X") or
   # diagonal
   (rows_159[1] and rows_159[2] and rows_159[3] == "X") or
   (rows_357[1] and rows_357[2] and rows_357[3] == "X"):
   Xwin=true

Ywin=false
   # horizontal
if (rows_123[1] and rows_123[2] and rows_123[3] == "Y") or
   (rows_456[1] and rows_456[2] and rows_456[3] == "Y") or
   (rows_789[1] and rows_789[2] and rows_789[3] == "Y") or
   # vertical
   (rows_147[1] and rows_147[2] and rows_147[3] == "Y") or
   (rows_258[1] and rows_258[2] and rows_258[3] == "Y") or
   (rows_369[1] and rows_369[2] and rows_369[3] == "Y") or
   # diagonal
   (rows_159[1] and rows_159[2] and rows_159[3] == "Y") or
   (rows_357[1] and rows_357[2] and rows_357[3] == "Y"):
   Ywin=true

if Xwin:
   return(parameter="X")
if Ywin:
   return(parameter="O")
