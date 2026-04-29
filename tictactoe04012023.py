#tictaktoe 03302023 will be the start of a challenge: making the game grid be
#    graphic button based
# code that supports graphics inserted below ##############################
from tkinter import *
# create main box with grid
gui = Tk(className='tictoe - graphic Buttons')
gui.geometry("350x290")
gui.resizable(False, False)
ipadding = {'ipadx': 10, 'ipady': 10}
gui.columnconfigure(2)
gui.rowconfigure(2)

#relocated from below
def clear_board():
    cleared_board="1|2|3,-+-+-,4|5|6,-+-+-,7|8|9"
    text1="1"
    text2="2"
    text3="3"
    text4="4"
    text5="5"
    text6="6"
    text7="7"
    text8="8"
    text9="9"
    
cleared_board="1|2|3,-+-+-,4|5|6,-+-+-,7|8|9"
text1="1"
text2="2"
text3="3"
text4="4"
text5="5"
text6="6"
text7="7"
text8="8"
text9="9"

# create button
button1 = Button(gui, text=text1, width=8, height=3, bg='#0052cc', fg='#ffffff',
                 activebackground='#0052cc', activeforeground='#aaffaa')
button2 = Button(gui, text=text2, width=8, height=3, bg='#0052cc', fg='#ffffff',
                 activebackground='#0052cc', activeforeground='#aaffaa')
button3 = Button(gui, text=text3, width=8, height=3, bg='#0052cc', fg='#ffffff',
                 activebackground='#0052cc', activeforeground='#aaffaa')

button4 = Button(gui, text=text4, width=8, height=3, bg='#0052cc', fg='#ffffff',
                 activebackground='#0052cc', activeforeground='#aaffaa')
button5 = Button(gui, text=text5, width=8, height=3, bg='#0052cc', fg='#ffffff',
                 activebackground='#0052cc', activeforeground='#aaffaa')
button6 = Button(gui, text=text6, width=8, height=3, bg='#0052cc', fg='#ffffff',
                 activebackground='#0052cc', activeforeground='#aaffaa')

button7 = Button(gui, text=text7, width=8, height=3, bg='#0052cc', fg='#ffffff',
                 activebackground='#0052cc', activeforeground='#aaffaa')
button8 = Button(gui, text=text8, width=8, height=3, bg='#0052cc', fg='#ffffff',
                 activebackground='#0052cc', activeforeground='#aaffaa')
button9 = Button(gui, text=text9, width=8, height=3, bg='#0052cc', fg='#ffffff',
                 activebackground='#0052cc', activeforeground='#aaffaa')

# add button to gui window
button1.grid(column=0, row=0, ipadx=20, ipady=20)
button2.grid(column=1, row=0, ipadx=20, ipady=20)
button3.grid(column=2, row=0, ipadx=20, ipady=20)

button4.grid(column=0, row=1, ipadx=20, ipady=20)
button5.grid(column=1, row=1, ipadx=20, ipady=20)
button6.grid(column=2, row=1, ipadx=20, ipady=20)

button7.grid(column=0, row=2, ipadx=20, ipady=20)
button8.grid(column=1, row=2, ipadx=20, ipady=20)
button9.grid(column=2, row=2, ipadx=20, ipady=20)

#will the program still work
#gui.mainloop()
#################################################################
#tictactoe.py
#these are the move positions: (down, across)
#      0,0 0,2 0,4
#      2,0 2,2 2,4
#      4,0 4,2 4,4
#   cleared_board="1|2|3,-+-+-,4|5|6,-+-+-,7|8|9"
#    text1="1"
#    text2="2"
#    text3="3"
#    text4="4"
#    text5="5"
#    text6="6"
#    text7="7"
#    text8="8"
#    text9="9"
    
def print_board(board_key):
    board_list = board_key.split(",")
    print (" ")
    print(board_list[0]) # 1|2|3
    print(board_list[1]) # -+-+-
    print(board_list[2]) # 4|5|6
    print(board_list[3]) # -+-+-
    print(board_list[4]) # 7|8|9
    print(" ")

def select_box(player, board_key):
    used=True
    while used==True:
        #select the grid box
        box = input("What grid box number do you want to put an "+player+" in? ")
        # box cannot be blank, if so then loop & do prompt again
        if box == ' ' or box == '' or box not in '123456789qQeE':
            print('Box number cannot be blank. Select box')
            print_board(board_key)
            continue
        box=str(box).upper()
        if box in 'QE':
            quit()
        # test if box has already been used.
        try:
            used=board_key.index(box)
        except:
            print('That box number not available. Pick a different box.')
            continue
    used=False
    if box in '123456789':
        board_key = board_key.replace(box,player)
    else:
        print('That box number not available. Pick a different box.')
    print("select box")
    print_board(board_key)
    return board_key 
         
def win_rows_build(board_key): 
    # verticals: row_147, row_258, row_369 
    # horizontals: row_123, row_456, row_789
    # diagonals: row_159, row_357

    # for each verticle, horizontal, diagonal:
    board_list = board_key.split(',')
    # build horizontal rows beginning with 1, 4, 7    
    row_123=row_456=row_789=0
    row_123=board_list[0][0]+board_list[0][2]+board_list[0][4]
    row_456=board_list[2][0]+board_list[2][2]+board_list[2][4] 
    row_789=board_list[4][0]+board_list[4][2]+board_list[4][4] 

    # build vertical row beginning with 1, 2, 3
    row_147=row_258=row_369=0
    row_147=board_list[0][0]+board_list[2][0]+board_list[4][0]
    row_258=board_list[0][2]+board_list[2][2]+board_list[4][2] 
    row_369=board_list[0][4]+board_list[2][4]+board_list[4][4]  
    # build diagonal rows biginning with 1, 3
    row_159=row_357=0
    row_159=board_list[0][0]+board_list[2][2]+board_list[4][4]
    row_357=board_list[0][4]+board_list[2][2]+board_list[4][0]
    
    # put rows in an list so they can be interated easily
    win_rows=[row_123, row_456, row_789, row_147, row_258, row_369, row_159, row_357]
    return win_rows 

def win_test(win_rows, turns):        
    # test X's or O's for winning configuration
    win_x='XXX'
    win_o='OOO'
    win_test_count = 0
    for row in win_rows:
        win_test_count += 1
        print(win_test_count)
        if row == win_x:
            print(row)
            print('\n********')
            print('*X wins*')
            print('********\n')
            restart_flag="Y"
            turns = 0
            return restart_flag, turns 
        elif row == win_o:
            print('\n********')
            print('*O wins*')
            print('********\n')     
            restart_flag="Y"
            turns = 0
            return restart_flag, turns 
    if turns >= 9:
        print('Tie. No winner')
        restart_flag = "Y"
        turns = 0
        return restart_flag, turns
    print('No winner yet. Keep playing.')
    restart_flag="N"
    return restart_flag, turns
            
def select_player():
    # player 1 selection of X or O
    player1="N"
    player2="N"
    while player1 not in 'XOQ':
        player1=input('player 1: Do you want to be "X" or "O" ?')
        player1=player1.upper()
        if player1=="X":
            player2="O"
        elif player1=="O":
            player2="X"
        elif player1=="Q":
            quit()
        else:
            print("Please enter X or O (or Q to end game): ")
        print("player 1 will go first as " + player1)
        print("player 2 will go second as " + player2)
        return player1, player2 
def go_nogo(board_key, restart_flag, turns):
    if turns == 0:
        ready_to_play = input("Are you ready to play? Y,N,Q: ")
        ready_to_play = ready_to_play.upper()
        while ready_to_play in "YNQ":
            if ready_to_play == 'Y':
                if turns == 0:
                    # start game
                    board_key=cleared_board
                    print("start:")
                    print_board(board_key)
                elif turns == 1:
                    board_key = cleared_board
                    print(board_key)
                # test if this round is done
                #elif turns >= 9:
                #    print('Tie. No winner')  # commented for debugging
                #    restart_flag = "Y"
                #    turns = 0
                #    return restart_flag, turns
                # player 1 make selection & after 3 check for win
                turns += 1              
                print('1-turns: ', turns) #debug
                board_key = select_box(player1, board_key)
                win_rows=win_rows_build(board_key) 
                restart_flag, turns=win_test(win_rows, turns)
                # test if this round is done
                if turns >= 9:
                    print('Tie. No vinner')  # commented for debugging
                    restart_flag = "Y"
                    turns = 0
                    return restart_flag, turns
                # player 2 make selection & after 3 check for win
                turns += 1
                print('2-turns: ', turns)
                # test if this round is done
                if turns >= 9:
                    print('Tie. No winner')  
                    restart_flag = "Y"
                    turns = 0
                    return restart_flag, turns
                board_key = select_box(player2, board_key)             
                win_rows=win_rows_build(board_key)
                restart_flag, turns=win_test(win_rows, turns)
            elif ready_to_play == "N":
                restart_flag = "N"
            else:
                quit()

    
#########################################################################################
#main
import time        
restart_flag='Y'
turns=0
clear_board()
while restart_flag in 'YNQ':
    if restart_flag=="Y":
        board_key=cleared_board
        print('Welcome to TicTacToe')
        # player 1 selection of X or O
        player1, player2=select_player()    
        restart_flag,turns=go_nogo(board_key,restart_flag,turns)
else:
    if restart_flag=="N" and turns>1:
        restart_flag, ready_to_play=go_nogo(board_key,restart_flag,turns)
        print('made it back from go_nogo')
    else:
        # quit game
        quit()
