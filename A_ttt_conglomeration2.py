#this not working right. no errors but replacments in grid_not holding
import ttt_func
Board = ttt_func.build_board()
print (Board[0])
print (Board[1])
print (Board[2])
print (Board[3])
print (Board[4])
print ("------------------")
player1, player2=ttt_func.select_player()
# do player1 then player2 alternately
idx=0
while (idx<9):
    #pick player for this round
    placeholder=ttt_func.isEven(idx)
    if (placeholder):
        player=player1
    else:
        player=player2
    # pick location (1-9) for this round
    grid_box = ttt_func.select_box(player)
    print("grid_box", grid_box)
    # select row to search for location
    print("idx", idx)
    idx3 = str(idx)
    if idx3 in "012":
        grid_row = 0
    elif idx3 in "345":
        grid_row = 2
    elif idx3 in "678":
        grid_row = 4
    #following 2 lines for debug
    print("grid_row", grid_row)
    # for row, see where selected location is and replace number with value of 'player'
    # iterate through row
    for idx2, grid_box in enumerate (Board[grid_row]):
        if grid_box == Board[grid_row][idx2]:
           print("grid_row, idx2, grid_box,", grid_row, idx2, grid_box,Board[grid_row][idx2])
           print (Board[grid_row][idx2])    
           blat = Board[grid_row].replace(Board[grid_row][idx2], player)
           print( blat)
           Board[grid_row]=blat
    idx=idx+1
print ("Board[grid_row]",Board[grid_row])
quit()
print ("------------------")
print (Board[0])
print (Board[1])
print (Board[2])
print (Board[3])
print (Board[4])
