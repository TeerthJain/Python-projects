"""
Made by Teerth Jain on 25/8/2020
"""

#Board
#display board
#play game
#handle turn
#check win
    #check row
    #check columns
    #check diagonals
#check tile
#flip player

#------------------GLOBAL VARIABLES---------------------------#

board = ["-", "-", "-", 
        "-", "-", "-", 
        "-", "-", "-", ]

game_still_going = True
current_player = 1

winner = None
current_player = "X"

#------------------END OF GLOBAL VARIABLES---------------------------#

def display_board():
    print(" ")
    print(" ")
    
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    print(" ")
    print(" ")


def play_game():
    #Displays board
    display_board()


    while game_still_going == True:
        handle_turn(current_player)
        check_for_winner()
    else:
        print("GAME OVER")

def handle_turn(cur_player):
    global current_player
    print(f"{cur_player}'s turn now'")
    position = input("Choose a position from 1 to 9: ")
    if position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("Invalid number")
        print(" ")
        print(" ")
        return

    position = int(position) - 1

    #Checking if the space is pre-used
    if board[position] != "-":
        print("You can't go there, try again")
        display_board()
        return

    board[position] = cur_player
    if cur_player == "X":
        current_player = "O"
    else:
        current_player = "X"
    
    #Just making up some space before and after showing the board

    display_board()
  

def check_if_game_over():
    global game_still_going
    if winner == "X" or winner == "O":
        print(f"Player {winner} WON!!")
        game_still_going = False
    elif '-' not in board:
        print("Noone wins")
        game_still_going = False
    return
    


def check_for_winner():
    #----------CHECKING ROWS-------------#
    global game_still_going
    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'
    if row1:
        print(board[0] + " WON")
        game_still_going = False
        return
    elif row2:
        game_still_going = False
        print(board[3] + " WON")
        return
    elif row3:
        game_still_going = False
        print(board[7] + " WON")
        return
    check_if_game_over()
    #----------CHECKING DIAGONALS-------------#
    dia1 = board[0] == board[4] == board[8] != '-'
    dia2 = board[2] == board[4] == board[6] != '-'
   
    if dia1:
        print(board[0] + " WON")
        game_still_going = False
        return
    elif dia2:
        game_still_going = False
        print(board[2] + " WON")
        return
    check_if_game_over()
    #------------CHECKING COLUNMS----------------------------#
    col1 = board[0] == board[3] == board[6] != '-'
    col2 = board[1] == board[4] == board[7] != '-'
    col3 = board[2] == board[5] == board[8] != '-'
    if col1:
        print(board[0] + " WON")
        game_still_going = False
        return
    elif col2:
        game_still_going = False
        print(board[1] + " WON")
        return
    elif col3:
        game_still_going = False
        print(board[2] + " WON")
        return
    check_if_game_over()



play_game()



