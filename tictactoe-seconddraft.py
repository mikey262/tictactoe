win_list = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]


def show_board(board): 
    print(board[0], board[1], board[2]) 
    print(board[3], board[4], board[5]) 
    print(board[6], board[7], board[8])

    
def check_winner(player_board):
    counter = 0
    for tuples in win_list:
        for ints in tuples:
            if ints in player_board:
                counter += 1
                if counter == 3:
                    break
                else:
                    continue
        if counter == 3:  
            return True
            print("winner")
        else:
            counter = 0

def play_again():
    answer = input("Do you want to play again? y/n: ")
    while answer.lower() not in ['y','n']:
        print("invalid response.  enter again.")
        answer = input("Do you want to play again? y/n: ")
    
    return answer.lower() == 'y'
           


#start logic now

restart = True

while restart == True:
    play = True
    x_board = [] 
    o_board = []
    draw_counter = 0
    board = [1,2,3,4,5,6,7,8,9]

    print("Play Tic Tac Toe! enter integers 1-9 for the following positions:") 
    show_board(board)

    while play == True:

        temp_x = 10
        while int(temp_x) not in board:
            print("Please choose an integer between 1-9 that hasn't already been picked:")
            temp_x = input("Player x - choose!:")
            if temp_x.isdigit() == False or int(temp_x) not in board:
                temp_x = 10
                continue
        
        temp_x = int(temp_x)
        x_board.append(temp_x)
        board[temp_x-1] = 'x'
        show_board(board)
        if check_winner(x_board): 
            print('x wins!')
            play = False
            repeat = play_again()
            if repeat == True:
                break
            else:
                restart = False
                break

        draw_counter += 1
        if draw_counter == 9:
            print("game over. no winner")
            play = False
            repeat = play_again()
            if repeat == True:
                break
            else:
                restart = False
                break



        temp_o = 10
        while int(temp_o) not in board:
            print("Please choose an integer between 1-9 that hasn't already been picked:")
            temp_o = input("Player x - choose!:")
            if temp_o.isdigit() == False or int(temp_o) not in board:
                temp_o = 10
                continue
        
        temp_o = int(temp_o)
        o_board.append(temp_o)
        board[temp_o-1] = 'o'
        show_board(board)
        if check_winner(o_board): 
            print('o wins!')
            play = False
            repeat = play_again()
            if repeat == True:
                break
            else:
                restart = False
                break

        draw_counter += 1
        if draw_counter == 9:
            print("game over. no winner")
            play = False
            repeat = play_again()
            if repeat == True:
                break
            else:
                restart = False
                break

    

    