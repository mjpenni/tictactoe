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
print ("------------------")
# Take turns: do player1 then player2 alternately for the 9 spots on the game grid
# in Python lingo that's 0-8
idx=0
while (idx<9):
    #pick player for this round: X or O
    placeholder=ttt_func.isEven(idx)
    if (placeholder):
        player=player1
    else:
        player=player2
    # pick location (1-9) for this round. Actual number 1-9 not Python 0-8
    grid_box = ttt_func.select_box(player)
    # select row to search for location
    # why isn't grid_row being set eadh time? Sometimes yes, sometimes no.
    for idx2 in range(0,9):
        if grid_box == "1":
            grid_row = 0
            break
        elif grid_box == "2":
            grid_row = 0
            break
        elif grid_box == "3":
            grid_row = 0
            break
        elif grid_box == "4":
            grid_row = 2
            break
        elif grid_box == "5":
            grid_row = 2
            break
        elif grid_box == "6":
            grid_row = 2
            break
        elif grid_box == "7":
            grid_row = 4
            break
        elif grid_box == "8":
            grid_row = 4
            break
        elif grid_box == "9":
            grid_row = 4
            break
        else:
            print ('box not found in grid')
    # see where selected location is and replace number with value of 'player'
    # iterate through row
    for idx2, grid_box2 in enumerate (Board[grid_row]):
        if grid_box == Board[grid_row][idx2]:
           blat = Board[grid_row].replace(Board[grid_row][idx2], player)
           Board[grid_row]=blat      
    idx=idx+1
print ("------------------")
#check for a win. 
print (ttt_func.victory_test(Board), "is the winner!")
print (Board[0])
print (Board[1])
print (Board[2])
print (Board[3])
print (Board[4])
