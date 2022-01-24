from main import plot
from main import figures
from main import board
from main import field 
from main import move_to
from check import check_move
from convert import name_of
# from compress import compress
import time

input('Press enter to start chess!')
plot(board)
# move_to(board, 2, 19)

# def for check what selected
def selected(c: int, board: list) -> str:
    return board[c-1]


a = 0

while a != -1: 
    a = int(input('enter a start field: '))
    print('selected ' + name_of(a, board) + ' at ' + str(a))
    if a == -1:
        print('great you broke it')
        break

    b = int(input('enter the aimed location: '))
    print('selected ' + name_of(b, board) + ' at ' + str(b))
    
    # check = input('make move? [y/n] \n')
    check = 'y'
    # case y and try move
    if check == 'y':
        if check_move(board, a, b) == True:
            move_to(board, a, b)
            plot(board)
        else: 
            print('Not a valid move!')
    # case if no
    elif check == 'n':
        print('nothing happened')
    # error case
    else: 
        print('Error #002')


    #
    # log var for what happened
    #

    

    # plot(board)



# do somewhere else


