import random

moves = ["R", "P", "S"]

player = None

while player not in moves:
    player = input("Pick an option between 'R', 'P' and 'S'\n")
    if player not in moves:
        print("Error, try again")

if player == 'R':
    player = "Rock"
elif player == 'P':
    player = "Paper"
elif player == 'S':
    player = "Scissors"

CPU = random.choice(moves)

if CPU == 'R':
    CPU = "Rock"
elif CPU == 'P':
    CPU = "Paper"
elif CPU == 'S':
    CPU = "Scissors"

if moves[0] == 'R':
    moves[0] = 'Rock'
    if moves[1] == 'P':
        moves[1] = 'Paper'
        if moves[2] == 'S':
            moves[2] = 'Scissors'

if player == CPU:
    print("Player ({}):CPU ({})".format(player,CPU))
    print("TIE")
elif player == 'Rock':
    if CPU == 'Scissors':
        print("Player ({}):CPU ({})".format(player,CPU))
        print("You won!")   
elif player == 'Paper':
    if CPU == 'Rock':
        print("Player ({}):CPU ({})".format(player,CPU))
        print("You won!") 
elif player == 'Scissors':
    if CPU == 'Paper':
        print("Player ({}):CPU ({})".format(player,CPU))
        print("You won!")           

    

