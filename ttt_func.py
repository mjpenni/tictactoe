#ttt_func.py
#tictacto game utilities (functions)
#select a player: X or O
def select_player():
    player1="N"
    while player1 not in 'XO':
        player1=input('player 1: Do you want to be X or O? ')
        if player1=="x":
            player1="X"
        elif player1=="o":
            player1="O"
        if player1=="X":
            player2="O"
        elif player1=="O":
            player2="X"
        else:
            print("Please enter X or O.")
    return (player1, player2)
#build the game grid
def build_board():
    temp_insane = ["1|2|3","-+-+-","4|5|6","-+-+-","7|8|9"]
    return temp_insane
#select a grid location
def select_box(player):
    box_local = input("What box number do you want to put an " + player +"? ")
    return box_local
#test if number is even or odd
# even is True and odd is False
def isEven(number):
    return number % 2 == 0
#check for 3 X's or 3 O's
def victory_test(grid):
    #check horizontal rows: 123, 456, 789
    #check vertical   rows: 147, 258, 369
    #check diagonal   rows: 159, 357
    #to start: win=False
    #each row is checked for 3 matching (X or O) entries
    #1 of 8 successful tests mean victory
    # horizontal
    row_123 = grid[0][0]+grid[0][2]+grid[0][4]
    row_456 = grid[2][0]+grid[2][2]+grid[2][4]
    row_789 = grid[4][0]+grid[4][2]+grid[4][4]
    if (row_123 or row_456 or row789) == "XXX":
       return "X"
    # vertical
    row_147 = grid[0][0]+grid[2][0]+grid[4][0]
    row_258 = grid[0][2]+grid[2][2]+grid[4][2]
    row_369 = grid[0][4]+grid[2][4]+grid[4][4]
    if (row_147 or row_258 or row_369) == "XXX":
       return "X"
    # diagonal
    row_159 = grid[0][0]+grid[2][2]+grid[4][4]
    row_357 = grid[0][4]+grid[2][2]+grid[4][0]
    if (row_159 or row_357) == "XXX":
       return "X"
    # horizontal
    row_123 = grid[0][0]+grid[0][2]+grid[0][4]
    row_456 = grid[2][0]+grid[2][2]+grid[2][4]
    row_789 = grid[4][0]+grid[4][2]+grid[4][4]
    if (row_123 or row_456 or row_789) == "OOO":
       return "O"
    # vertical
    row_147 = grid[0][0]+grid[2][0]+grid[4][0]
    row_258 = grid[0][2]+grid[2][2]+grid[4][2]
    row_369 = grid[0][4]+grid[2][4]+grid[4][4]
    if (row_147 or row_258 or row_369) == "OOO":
       return "O"
    # diagonal
    row_159 = grid[0][0]+grid[2][2]+grid[4][4]
    row_357 = grid[0][4]+grid[2][2]+grid[4][0]
    if (row_159 or row_357) == "OOO":
       return "O"

