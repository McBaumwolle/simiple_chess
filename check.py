from main import board

# allowed moves for w, -1 when blk
# all potentially allowed movements
# check later if all are allowed
# allowed_p = [7, 8, 9, 15, 16, 17]


#
# check if a has fig in in for begin
#


def check_move(board: list, a: int, b: int) -> bool: 
    msg = ''
    legit = False
    team = 'w'
    team_value = 1
    allowed = []

    if a > 64 or a < 1 or b > 64 or b < 1:
        return False 
    
    if board[a - 1][0] == 'b':
        print('team black')
        team = 'b'
        team_value = -1

        board.reverse()
        a = -a + 65
        b = -b + 65

    # fig = pawn
    if board[a-1][1] == 'p':
        
        allowed = [7, 8, 9]

        if a in [57, 58, 59, 60, 61, 62, 63, 64]:
            print('-- pawn at end of board --\n')
            return False
        
        # check if left or right edge
        if a in [1, 9, 17, 25, 33, 41, 49]:
            allowed.remove(7)
        elif a in [8, 16, 24, 32, 40, 48]:
            allowed.remove(9)
        
        # add double move if first move
        if a in [10, 11, 12, 13, 14, 15]:
            allowed.extend((15, 16, 17))
        elif a == 9:
            allowed.extend((16, 17))
        elif a == 16: 
            allowed.extend((15, 16))
        
        # remove straight forward if it's not empty
        if board[a+8] != '   ':
            allowed.remove(8)
        
        for i in [7, 9, 15, 17]:
            if a+i < 65:
                if board[a+i] == '   ' and i in allowed:
                    allowed.remove(i)
        
    # fig = rook
    if board[a-1][1] == 'r':
        allowed = [-1, -2, -3, -4, -5, -6, -7,
                    1, 2, 3, 4, 5, 6, 7,
                    -8, -16, -24, -32, -40, -48, -56,
                    8, 16, 24, 32, 40, 48, 56
                  ]

        #case side 1/4
        if a in [1, 8, 16, 24, 32, 40, 48, 56]:
            for i in (-1, -2, -3, -4, -5, -6, -7):
                allowed.remove(i)

    # use math here please
    # check onenote 
    

    
    # checks if fig is ???
    elif board[a - 1][1] == 'p':
        print('404')

    else: 
        print('404')


    
    if team_value == -1: 
        board.reverse()
        a = -a + 65
        b = -b + 65
    

    if abs(b-a) in allowed: 
        legit = True

        if board[b-1] != '   ':
            msg = msg + '-- removed ' + board[b-1] + ' from the field --\n'


    print(msg)
    return legit


