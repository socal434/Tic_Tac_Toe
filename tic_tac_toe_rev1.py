from __future__ import print_function
from random import randint


def play_tic_tac_toe():
    print ("Let's Play!")
    
    board = [['_', '_', '_'], ['_' , '_' , '_'], ['_' , '_' , '_']]
    
    #This function generates the 3 X 3 board that will be used in the game
    def display_board():
        for row in board:
            print (' '.join(row))
    
    #This function asks the player for an input and places it on the board
    def player_input(player):
        while True:
            x = ''
            y = ''
            while x not in '1 2 3 4 5 6 7 8 9 0'.split():
                selection_row_msg = 'Player %d enter your row selection: ' %(player)
                x = raw_input(selection_row_msg)
            x = int(x)
            selection_row = x - 1
            while y not in '1 2 3 4 5 6 7 8 9 0'.split():
                selection_column_msg = 'Player %d enter your column selection: ' %(player)
                y = raw_input(selection_column_msg)
            y = int(y)
            selection_column = y - 1
            board_row_length = len(board) #length of board from top to bottom
            board_column_length = len(board[0]) #length of board from left to right
            #next checks for both players if the selection is within the acceptable range of the board and is not already used
            if player == 1:
                if (x in range(1, board_row_length + 1) and y in range(1, board_column_length + 1) and
                (board[selection_row][selection_column] == '_')):
                    board[int(selection_row)].pop(int(selection_column))
                    board[int(selection_row)].insert(int(selection_column),'x')
                    display_board()
                    check_win()
                    player = 2
                else:
                    print ('Not a valid choice')                   
            elif player == 2:
                if (x in range(1, board_row_length + 1) and y in range(1, board_column_length + 1) and
                (board[selection_row][selection_column] == '_')):
                    board[int(selection_row)].pop(int(selection_column))
                    board[int(selection_row)].insert(int(selection_column),'o')
                    display_board()
                    check_win()
                    player = 1
                else:
                    print ('Not a valid choice')

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
        while True:
            choice = raw_input('Would you like to play again? Yes or No.')
            choice = choice.lower()
            if choice == 'yes':
                play_tic_tac_toe()
            elif choice == 'no':
                print('Thank you for playing')
                quit()
            else:
                print('Not a valid answer')
                    
        

    #This function randomly chooses a player to start
    def game_start():
        player = randint(1,2)   
        player_input(player)
    
        

    display_board()
    game_start()


