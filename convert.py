from main import figures
from main import board
from main import field 
from main import move_to


# print(board)
# move_to(board, 2, 25)
# print(board)


# compresses the board, not very convenient
def compress(board: list) -> str:
    set = ''
    for i in range(0, 64): 
        if board[i] != '   ': 
            set = set + str(i + 1) + board[i] + '.'
        # else: 
            #     set = set + str(i + 1) + '0' + '.'
    set = set[0:len(set) - 1]
    return set
       
# print(compress(board))


# expand the string back to board
def expand(board: str) -> list: 
    print('404')


# export name of selected fig or empty
def name_of(c: int, board: list) -> str:
    out = ''
    fig = board[c-1]
    if fig == '   ':
        return 'empty field'
    # check w or b
    else: 
        if fig[0] == 'w':
            out = out + 'white'
        elif fig[0] == 'b':
            out = out + 'black'
        else:
            print('Error #001')
            # error event
            exit()

        if fig[1] == 'p':
            out = out + ' pawn no' + fig[2]
        elif fig[1] == 'k':
            out = out + ' knight no' + fig[2]
        elif fig[1] == 'b':
            out = out + ' bishop no' + fig[2]
        
        #rest here


    return out


     
# print(name_of(9, board))
# print(name_of(2, board))
# print(name_of(3, board))

