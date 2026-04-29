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