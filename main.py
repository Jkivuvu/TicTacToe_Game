from os import system, name


def clear():
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')

    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')


def winner(P1_symbol, P2_symbol, turns):
    global is_winner
    # Checking the grid horizontally for player 1
    if T[0] == P1_symbol and T[1] == P1_symbol and T[2] == P1_symbol:
        print('Player 1 is the winner!')
        is_winner = True
    elif T[3] == P1_symbol and T[4] == P1_symbol and T[5] == P1_symbol:
        print('Player 1 is the winner!')
        is_winner = True
    elif T[6] == P1_symbol and T[7] == P1_symbol and T[8] == P1_symbol:
        print('Player 1 is the winner!')
    # Checking the grid horizontally for player 2
    if T[0] == P2_symbol and T[1] == P2_symbol and T[2] == P2_symbol:
        print('Player 2 is the winner!')
        is_winner = True
    elif T[3] == P2_symbol and T[4] == P2_symbol and T[5] == P2_symbol:
        print('Player 2 is the winner!')
        is_winner = True
    elif T[6] == P2_symbol and T[7] == P2_symbol and T[8] == P2_symbol:
        print('Player 2 is the winner!')
        is_winner = True
    # Checking the grid vertically for player 1
    elif T[0] == P1_symbol and T[3] == P1_symbol and T[6] == P1_symbol:
        print('Player 1 is the winner!')
        is_winner = True
    elif T[1] == P1_symbol and T[4] == P1_symbol and T[7] == P1_symbol:
        print('Player 1 is the winner!')
        is_winner = True
    elif T[2] == P1_symbol and T[5] == P1_symbol and T[8] == P1_symbol:
        print('Player 1 is the winner!')
        is_winner = True
    # Checking the grid vertically for player 2
    elif T[0] == P2_symbol and T[3] == P2_symbol and T[6] == P2_symbol:
        print('Player 2 is the winner!')
        is_winner = True
    elif T[1] == P2_symbol and T[4] == P2_symbol and T[7] == P2_symbol:
        print('Player 2 is the winner!')
        is_winner = True
    elif T[2] == P2_symbol and T[5] == P2_symbol and T[8] == P2_symbol:
        print('Player 2 is the winner!')
        is_winner = True
    # Checking the grid diagonally for player 1
    elif T[0] == P1_symbol and T[4] == P1_symbol and T[8] == P1_symbol:
        print('Player 1 is the winner!')
        is_winner = True
    elif T[2] == P1_symbol and T[4] == P1_symbol and T[6] == P1_symbol:
        print('Player 1 is the winner!')
        is_winner = True
    # Checking the grid diagonally for player 2
    elif T[0] == P2_symbol and T[4] == P2_symbol and T[8] == P2_symbol:
        print('Player 2 is the winner!')
        is_winner = True
    elif T[2] == P2_symbol and T[4] == P2_symbol and T[6] == P2_symbol:
        print('Player 2 is the winner!')
        is_winner = True
    else:
        if turns >= 9:
            print('It is a draw!')


play_game = None


while play_game != False:
    choice_to_play = input('Do you want to play a game? Y or N:\n').capitalize()
    if choice_to_play == 'N':
        play_game = False

    elif choice_to_play == 'Y':

        play_game = True
        clear()
        T = [1, 2, 3,
             4, 5, 6,
             7, 8, 9]
        P1_symbol = ''
        P2_symbol = ''
        is_winner = None
        grid = f"{'     '}_{T[0]}_|_{T[1]}_|_{T[2]}_\n{'     '}_{T[3]}_|_{T[4]}_|_{T[5]}_\n{'     '}_{T[6]}_|_{T[7]}_|_{T[8]}_"
        while P1_symbol != 'X' or P1_symbol != 'O':
            P1_symbol = input('Which symbol would you like? X or O\n').capitalize()
            print(P1_symbol)
            if P1_symbol == 'X' or P1_symbol == 'O':
                break
            else:
                print('You have picked a wrong entry! please try again')

        if P1_symbol == 'X':
            P2_symbol = 'O'
        else:
            P2_symbol = 'X'
        turns = 0
        while turns <= 9:
            clear()
            if turns >= 9:
                break
            grid = f"{'     '}_{T[0]}_|_{T[1]}_|_{T[2]}_\n{'     '}_{T[3]}_|_{T[4]}_|_{T[5]}_\n{'     '}_{T[6]}_|_{T[7]}_|_{T[8]}_"
            print(grid)
            clear()
            winner(P1_symbol=P1_symbol, P2_symbol=P2_symbol, turns=turns)
            if is_winner:
                print(grid)
                break
            else:
              clear()
              print(grid)
            player_pick1 = ''
            player_pick2 = ''
            while not player_pick1 in T:
                player_pick1 = int(input('Player 1 Pick a number \n'))
                if not player_pick1 in T:
                    print('The space you have picked has been chosen or is does not exist.\n Pick another space')

            if player_pick1 in T:
                T[T.index(player_pick1)] = P1_symbol
                grid = f"{'     '}_{T[0]}_|_{T[1]}_|_{T[2]}_\n{'     '}_{T[3]}_|_{T[4]}_|_{T[5]}_\n{'     '}_{T[6]}_|_{T[7]}_|_{T[8]}_"
                winner(P1_symbol=P1_symbol, P2_symbol=P2_symbol, turns=turns)
                print(grid)
                clear()
                winner(P1_symbol=P1_symbol, P2_symbol=P2_symbol, turns=turns)
                if is_winner:
                  print(grid)
                  break
                else:
                  clear()
                  print(grid)
            turns += 1
            if turns >= 9:
                break
            while not player_pick2 in T:
                player_pick2 = int(input('Player 2 Pick a number \n'))
                if not player_pick1 in T:
                    print('The space you have picked has been chosen or is does not exist.\n Pick another space')
            if player_pick2 in T:
                T[T.index(player_pick2)] = P2_symbol
            turns += 1
        if turns >= 9:
          winner(P1_symbol=P1_symbol, P2_symbol=P2_symbol, turns=turns)
