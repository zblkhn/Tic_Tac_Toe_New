main_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player_turn = ' '
player_start = 'x'

def board(list1):
    print('┌─────┬─────┬─────┐')
    print('│ ',list1[0], ' │ ',list1[1],' │ ',list1[2],' │')
    print('├─────┼─────┼─────┤')
    print('│ ',list1[3],' │ ',list1[4],' │ ',list1[5],' │')
    print('├─────┼─────┼─────┤')
    print('│ ',list1[6],' │ ',list1[7],' │ ',list1[8],' │')
    print('└─────┴─────┴─────┘')

def welcome():
    global main_list
    global player_turn
    global player_start
    print('\033[33mWelcome to the Tic Tac Toe game!!')
    print('Please remember the place of these numbers in the table\033[0m')
    list1_9 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("\033[34m")
    board(list1_9)
    print("\033[0m")
    main_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    print('plyer one is x and plyer two is o')
    if player_start == 'x':
        player_start = 'o'
    else:
        player_start = 'x'
    player_turn = player_start
    game_start()

def game_start():
    global player_turn
    if player_turn == 'x':
        player_turn = 'o'
    else:
        player_turn = 'x'
    game_check()
    play_game()

def game_check():
    if main_list[0] == main_list[1] and main_list[0] == main_list[2] and main_list[0] != ' ':
        how_win(main_list[0])
    elif main_list[3] == main_list[4] and main_list[3] == main_list[5] and main_list[3] != ' ':
        how_win(main_list[3])
    elif main_list[6] == main_list[7] and main_list[6] == main_list[8] and main_list[6] != ' ':
        how_win(main_list[6])
    elif main_list[0] == main_list[3] and main_list[0] == main_list[6] and main_list[0] != ' ':
        how_win(main_list[0])
    elif main_list[1] == main_list[4] and main_list[1] == main_list[7] and main_list[1] != ' ':
        how_win(main_list[1])
    elif main_list[2] == main_list[5] and main_list[2] == main_list[8] and main_list[2] != ' ':
        how_win(main_list[2])
    elif main_list[0] == main_list[4] and main_list[0] == main_list[8] and main_list[0] != ' ':
        how_win(main_list[0])
    elif main_list[2] == main_list[4] and main_list[2] == main_list[6] and main_list[2] != ' ':
        how_win(main_list[2])
    if game_end():
        print('Game is draw!!')
        yorn = input('Play again?(y/n) ')
        if yorn =='y':
            welcome()
        else:
            exit()

def how_win(xoro):
    if xoro == 'x':
        print("\033[36mCongratulationsو Player x has won!!\033[0m")
    elif xoro == 'o':
        print("\033[36mCongratulationsو Player o has won!!\033[0m")
    yorn = input('Play again?(y/n) ')
    if yorn == 'y':
        welcome()
    else:
        exit()

def game_end():
    for item in main_list:
        if item == ' ':
            return False
    return True

def play_game():
    print("\033[32mIt's ", player_turn, "'s turn to play\033[0m")
    sel_num = int(input('Enter a number between 1 and 9: '))
    if sel_num >= 1 and sel_num <= 9:
        if main_list[sel_num - 1] == ' ':
            main_list[sel_num - 1] = player_turn
        else:
            print("\033[31mThe entered number is duplicate!!\033[0m")
            play_game()
        board(main_list)
        game_start()
    else:
        print('\033[31mThe entered number is out of range!!\033[0m')
        play_game()

welcome()
