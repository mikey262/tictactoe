board = [1,2,3,4,5,6,7,8,9]
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

def check_board(boardname):
    i = 0
    for n in boardname:
        if n == 'o' or n == 'x':
            i += 1
    if i == 9:
        return True
        
#start game 
print("Play Tic Tac Toe! enter integers 1-9 for the following positions:") 
print("Let's Begin!")
show_board(board)


#start logic now
winner = False
x_board = [] 
o_board = []

while winner == False:
    
    temp_x = int(input("Player x - choose!:"))
    x_board.append(temp_x)
    board[temp_x-1] = 'x'
    show_board(board)
    if check_winner(x_board): 
        winner = True
        print('x wins!')
        break
    if check_board(board):
        print("game over. no winner")
        break
    
    temp_o = int(input("Player o - choose!:"))
    o_board.append(temp_o)
    board[temp_o-1] = 'o'
    show_board(board)
    if check_winner(o_board): 
        winner = True
        print('o wins!')
        break
    if check_board(board):
        print("game over. no winner")
        break
    
    