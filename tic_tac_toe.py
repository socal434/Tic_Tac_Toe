from __future__ import print_function
from random import randint
def play_tic_tac_toe():
    print ("Let's Play!")
    
    board = [['_', '_', '_'], ['_' , '_' , '_'], ['_' , '_' , '_']]
    
    #This function generates the 3 X 3 board that will be used in the game
    def display_board():
        for row in board:
            print (' '.join(row))

    #This function asks for player one to make an input
    def player_one_input():
        print ('Player one enter your row selection: ')
        selection_row = int(raw_input()) #selects which row
        print ('Player one enter your column selection: ')
        selection_column = int(raw_input()) #selects which column
        board_row_length = len(board) #length of board from top to bottom
        board_column_length = len(board[0]) #length of board from left to right
        #next checks if the selection is within the acceptable range of the board and is not already used
        if (selection_row in range(1, board_row_length + 1) and selection_column in range(1, board_row_length + 1) and
            (board[selection_row - 1][selection_column - 1] == '_')):
            board[int(selection_row) - 1].pop(int(selection_column) - 1)
            board[int(selection_row) - 1].insert(int(selection_column) - 1,'x')
            for row in board:
                print (' '.join(row))
            check_win()
            player_two_input()
        else:
            print ('Not a valid choice')
            player_one_input()

    #This function asks for player two to make an input
    def player_two_input():
        print ('Player two enter your row selection: ')
        selection_row = int(raw_input()) #selects which row
        print ('Player two enter your column selection: ')
        selection_column = int(raw_input()) #selects which column
        board_row_length = len(board) #length of board from top to bottom
        board_column_length = len(board[0]) #length of board from left to right
        #next checks if the selection is within the acceptable range of the board and is not already used
        if (selection_row in range(1, board_row_length + 1) and selection_column in range(1, board_row_length + 1) and
            (board[selection_row - 1][selection_column - 1] == '_')):
            board[int(selection_row) - 1].pop(int(selection_column) - 1)
            board[int(selection_row) - 1].insert(int(selection_column) - 1,'o')
            for row in board:
                print (' '.join(row))
            check_win()
            player_one_input()
        else:
            print ('Not a valid choice')
            player_two_input()

    #This function checks to see if somebody won the game or is the game has no more valid moves
    def check_win():
        blank_space = 0
        if ((board[0][0] == 'x' and board[0][1] == 'x' and board[0][2] == 'x')
            or (board[0][0] == 'o' and board[0][1] == 'o' and board[0][2] == 'o')
            or (board[1][0] == 'x' and board[1][1] == 'x' and board[1][2] == 'x')
            or (board[1][0] == 'o' and board[1][1] == 'o' and board[1][2] == 'o')
            or (board[2][0] == 'x' and board[2][1] == 'x' and board[2][2] == 'x')
            or (board[2][0] == 'o' and board[2][1] == 'o' and board[2][2] == 'o')
            or (board[0][0] == 'x' and board[1][0] == 'x' and board[2][0] == 'x')
            or (board[0][0] == 'o' and board[1][0] == 'o' and board[2][0] == 'o')
            or (board[0][1] == 'x' and board[1][1] == 'x' and board[2][1] == 'x')
            or (board[0][1] == 'o' and board[1][1] == 'o' and board[2][1] == 'o')
            or (board[0][2] == 'x' and board[1][2] == 'x' and board[2][2] == 'x')
            or (board[0][2] == 'o' and board[1][2] == 'o' and board[2][2] == 'o')
            or (board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x')
            or (board[0][0] == 'o' and board[1][1] == 'o' and board[2][2] == 'o')
            or (board[0][2] == 'x' and board[1][1] == 'x' and board[2][0] == 'x')
            or (board[0][2] == 'o' and board[1][1] == 'o' and board[2][0] == 'o')):
            print('You Win!!!!')
            play_again()
        
        else:
            for row in board:
                for item in row:
                    if item == '_':
                        blank_space += 1
            if blank_space == 0:
                play_again()
        

    #This function asks if they want to play again
    def play_again():
        print('Would you like to play again? Yes or No.')
        choice = raw_input()
        if choice == 'Yes' or choice == 'yes':
            play_tic_tac_toe()
        elif choice == 'No' or choice == 'no':
            print('Thank you for playing')
            quit()
        else:
            print('Not a valid answer')
            play_again()
        

    #This function randomly chooses a player to start    
    def game_start():
        player = randint(1,2)
        if player == 1:
            player_one_input()
        elif player == 2:
            player_two_input()
        

    display_board()
    game_start()


