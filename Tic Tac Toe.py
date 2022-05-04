spots = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
turns = 0
winnerX = False
winnerO = False
game = True

def turn(player):
    global turns
    if player == 'Player 1':
        print("Player 1")  
        mark = input("Which square would you like to mark? ")
        if mark == '1':
            if spots[0] == 'X' or spots[0] == 'O':
                print("That spot is already taken. Try again.")
                turn('Player 1')
            else:
                spots[0] = 'X'
                turns = turns + 1
        elif mark == '2':
            if spots[1] == 'X' or spots[1] == 'O':
                print("That spot is already taken. Try again.")
                turn('Player 1')
            else:
                spots[1] = 'X'
                turns = turns + 1
        elif mark == '3':
            if spots[2] == 'X' or spots[2] == 'O':
                print("That spot is already taken. Try again.")
                turn('Player 1')
            else:
                spots[2] = 'X'
                turns = turns + 1
        elif mark == '4':
            if spots[3] == 'X' or spots[3] == 'O':
                print("That spot is already taken. Try again.")
                turn('Player 1')
            else:
                spots[3] = 'X'
                turns = turns + 1
        elif mark == '5':
            if spots[4] == 'X' or spots[4] == 'O':
                print("That spot is already taken. Try again.")
                turn('Player 1')
            else:
                spots[4] = 'X'
                turns = turns + 1
        elif mark == '6':
            if spots[5] == 'X' or spots[5] == 'O':
                print("That spot is already taken. Try again.")
                turn('Player 1')
            else:
                spots[5] = 'X'
                turns = turns + 1
        elif mark == '7':
            if spots[6] == 'X' or spots[6] == 'O':
                print("That spot is already taken. Try again.")
                turn('Player 1')
            else:
                spots[6] = 'X'
                turns = turns + 1
        elif mark == '8':
            if spots[7] == 'X' or spots[7] == 'O':
                print("That spot is already taken. Try again.")
                turn('Player 1')
            else:
                spots[7] = 'X'
                turns = turns + 1
        elif mark == '9':
            if spots[8] == 'X' or spots[8] == 'O':
                print("That spot is already taken. Try again.")
                turn('Player 1')
            else:
                spots[8] = 'X'
                turns = turns + 1
        else:
            print('Sorry, that is not a spot on the board. Try again')
            turn('Player 1')
           

    elif player == 'Player 2':
        print("Player 2")
        mark = input("Which square would you like to mark? ")
        if mark == '1':
            if spots[0] == 'X' or spots[0] == 'O':
                print("That spot is already taken. Try again.")
                turn('Player 2')
            else:
                spots[0] = 'O'
                turns = turns + 1
        elif mark == '2':
            if spots[1] == 'X' or spots[1] == 'O':
                print("That spot is already taken. Try again.")
                turn('Player 2')
            else:
                spots[1] = 'O'
                turns = turns + 1
        elif mark == '3':
            if spots[2] == 'X' or spots[2] == 'O':
                print("That spot is already taken. Try again.")
                turn('Player 2')
            else:
                spots[2] = 'O'
                turns = turns + 1
        elif mark == '4':
            if spots[3] == 'X' or spots[3] == 'O':
                print("That spot is already taken. Try again.")
                turn('Player 2')
            else:
                spots[3] = 'O'
                turns = turns + 1
        elif mark == '5':
            if spots[4] == 'X' or spots[4] == 'O':
                print("That spot is already taken. Try again.")
                turn('Player 2')
            else:
                spots[4] = 'O'
                turns = turns + 1
        elif mark == '6':
            if spots[5] == 'X' or spots[5] == 'O':
                print("That spot is already taken. Try again.")
                turn('Player 2')
            else:
                spots[5] = 'O'
                turns = turns + 1
        elif mark == '7':
            if spots[6] == 'X' or spots[6] == 'O':
                print("That spot is already taken. Try again.")
                turn('Player 2')
            else:
                spots[6] = 'O'
                turns = turns + 1
        elif mark == '8':
            if spots[7] == 'X' or spots[7] == 'O':
                print("That spot is already taken. Try again.")
                turn('Player 2')
            else:
                spots[7] = 'O'
                turns = turns + 1
        elif mark == '9':
            if spots[8] == 'X' or spots[8] == 'O':
                print("That spot is already taken. Try again.")
                turn('Player 2')
            else:
                spots[8] = 'O'
                turns = turns + 1
def check_for_win():
    global winnerX
    global winnerO
    #row win
    if spots[0] == spots[1] and spots[1] == spots[2] or spots[3] == spots[4] and spots[4] == spots[5] or spots[6] == spots[7] and spots[7] == spots[8]:
        if spots[0] == 'X' or spots[3] == 'X' or spots[6] == 'X':
            print("We have a winner!")
            winnerX = True
        if spots[0] == 'O' or spots[3] == 'O' or spots[6] == 'O':
            print("We have a winner!")
            winnerO = True
   
    #column win
    elif spots[0] == spots[3] and spots[3] == spots[6] or spots[1] == spots[4] and spots[4] == spots[7] or spots[2] == spots[5] and spots[5] == spots[8]:
        if spots[0] == 'X' or spots[1] == 'X' or spots[2] == 'X':
            print("We have a winner!")
            winnerX = True
        elif spots[0] == 'O' or spots[1] == 'O' or spots[2] == 'O':
            print("We have a winner!")
            winnerO = True
    
    #diagonal win
    elif spots[0] == spots[4] and spots[4] == spots[8] or spots[2] == spots[4] and spots[4] == spots[6]:
        if spots[0] == 'X' or spots[2] == 'X':
            print("We have a winner!")
            winnerX = True
        elif spots[0] == 'O' or spots[2] == 'O':
            print("We have a winner!")
            winnerO = True
    


while game == True:
    spots = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    turns = 0
    print(f"{spots[0]} | {spots[1]} | {spots[2]} \n"
        "--------- \n"
        f"{spots[3]} | {spots[4]} | {spots[5]} \n"
        "--------- \n"
        f"{spots[6]} | {spots[7]} | {spots[8]}")

    print("Let's play Tic-Tac-Toe!")
    print("The first player will be X and the second player will be O.")
    game = False

    #game loop
    while winnerX == False and winnerO == False:
        #player 1 turn
        turn('Player 1')
        print(f"{spots[0]} | {spots[1]} | {spots[2]} \n"
        "--------- \n"
        f"{spots[3]} | {spots[4]} | {spots[5]} \n"
        "--------- \n"
        f"{spots[6]} | {spots[7]} | {spots[8]}")
        check_for_win()
        if winnerX == True:
            print("Congrats Player 1! You won!")
            play_again = input("Do you want to play again? (y/n) ")
            if play_again == 'y':
                game = True
                winnerX = False
            elif play_again == 'n':
                print("See you next time then! ")
                break

        #player 2 turn
        turn('Player 2')
        print(f"{spots[0]} | {spots[1]} | {spots[2]} \n"
        "--------- \n"
        f"{spots[3]} | {spots[4]} | {spots[5]} \n"
        "--------- \n"
        f"{spots[6]} | {spots[7]} | {spots[8]}")
        check_for_win()
        if winnerO == True:
            print("Congrats Player 2! You won!")
            play_again = input("Do you want to play again? (y/n) ")
            if play_again == 'y':
                game = True
                winnerO = False
            elif play_again == 'n':
                print("See you next time then! ")
                break

        if turns == 9:
            print("Its a draw.")
            play_again = input("Do you want to play again? (y/n) ")
            if play_again == 'y':
                game = True
            elif play_again == 'n':
                print("See you next time then! ")
                break

    
    
