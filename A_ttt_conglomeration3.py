#this not working right. no errors but replacments in grid_not holding
import ttt_func
Board = ttt_func.build_board()
print (Board[0])
print (Board[1])
print (Board[2])
print (Board[3])
print (Board[4])
print ("------------------")
#select player number 1 as X or O. player number 2 is the other one
player1, player2=ttt_func.select_player()
# Take turns: do player1 then player2 alternately for the 9 spots on the game grid
# in Python lingo that's 0-8
#idx=0
#while (idx<9):
#or
for idx in range(0,9):
    #pick player for this round: X or O
    placeholder=ttt_func.isEven(idx)
    if (placeholder):
        player=player1
    else:
        player=player2
    # pick location (1-9) for this round. Actual number 1-9 not Python 0-8
    grid_box = ttt_func.select_box(player)
    print(" 26 grid_box", grid_box)
    # select row to search for location
    print("28 idx", idx)
#    idx3 = str(idx)
    # why isn't grid_row being set eadh time? Sometimes yes, sometimes no.
    if str(idx) in '012':
        grid_row = 0
    elif str(idx) in '345':
        grid_row = 2
    elif str(idx) in '678':
        grid_row = 4
    else:
        print ('box not found in grid')
    print ("39------------------",idx, grid_row)
    #following line for debug
    print("41 grid_row grid_box", grid_row, grid_box)
    # for row, see where selected location is and replace number with value of 'player'
    # iterate through row
    for idx2, grid_box2 in enumerate (Board[grid_row]):
        print ("45 ------------------", grid_row, grid_box2)
        if grid_box == Board[grid_row][idx2]:
           print ("47 ------------------")
           print ("48 grid_row, idx2, grid_box,Board[grid_row]", grid_row, idx2, grid_box2,Board[grid_row][idx2])
           print ("49 Board[grid_row][idx2])",Board[grid_row][idx2])    
           blat = Board[grid_row].replace(Board[grid_row][idx2], player)
           print( "51", blat)
           Board[grid_row]=blat
    print("53 ---------------")       
#idx=idx+1
print ("55 Board[grid_row]",Board[grid_row])
print ("56 ------------------")
print (Board[0])
print (Board[1])
print (Board[2])
print (Board[3])
print (Board[4])
#seems like a good place to check for a win. 