spots = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
turns = 0

def turn(player):
    global turns
    if player == 'Player 1':
        print("Player 1")  
        mark = input("Which square would you like to mark? ")
        if mark == '1':
            spots[0] = 'X'
            turns = turns + 1
        elif mark == '2':
            spots[1] = 'X'
            turns = turns + 1
        elif mark == '3':
            spots[2] = 'X'
            turns = turns + 1
        elif mark == '4':
            spots[3] = 'X'
            turns = turns + 1
        elif mark == '5':
            spots[4] = 'X'
            turns = turns + 1
        elif mark == '6':
            spots[5] = 'X'
            turns = turns + 1
        elif mark == '7':
            spots[6] = 'X'
            turns = turns + 1
        elif mark == '8':
            spots[7] = 'X'
            turns = turns + 1
        elif mark == '9':
            spots[8] = 'X'
            turns = turns + 1
        else:
            print('Sorry, that is not a spot on the board.')
            turns = turns + 1

    elif player == 'Player 2':
        print("Player 2")
        mark = input("Which square would you like to mark? ")
        if mark == '1':
            spots[0] = 'O'
            turns = turns + 1
        elif mark == '2':
            spots[1] = 'O'
            turns = turns + 1
        elif mark == '3':
            spots[2] = 'O'
            turns = turns + 1
        elif mark == '4':
            spots[3] = 'O'
            turns = turns + 1
        elif mark == '5':
            spots[4] = 'O'
            turns = turns + 1
        elif mark == '6':
            spots[5] = 'O'
            turns = turns + 1
        elif mark == '7':
            spots[6] = 'O'
            turns = turns + 1
        elif mark == '8':
            spots[7] = 'O'
            turns = turns + 1
        elif mark == '9':
            spots[8] = 'O'
            turns = turns + 1
        else:
            print('Sorry, that is not a spot on the board.')
            turns = turns + 1
    print(f"{spots[0]} | {spots[1]} | {spots[2]} \n"
    "--------- \n"
    f"{spots[3]} | {spots[4]} | {spots[5]} \n"
    "--------- \n"
    f"{spots[6]} | {spots[7]} | {spots[8]}")

def win():
    pass

print(f"{spots[0]} | {spots[1]} | {spots[2]} \n"
    "--------- \n"
    f"{spots[3]} | {spots[4]} | {spots[5]} \n"
    "--------- \n"
    f"{spots[6]} | {spots[7]} | {spots[8]}")


print("Let's play Tic-Tac-Toe!")
print("The first player will be X and the second player will be O.")
while turns < 9:
    pass