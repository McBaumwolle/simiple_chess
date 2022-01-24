# positions =    {
#     'wr1': 1, 'wk1': 2, 'wb1': 3, 'wq': 4, 'wk': 5, 'wb2': 6, 'wk2': 7, 'wr': 8,
#     'wp1': 9, 'wp2': 10, 'wp3': 11, 'wp4': 12, 'wp5': 13, 'wp6': 14, 'wp7': 15, 'wp8': 16,
#     'br1': 49, 'bk1': 50, 'bb1': 51, 'bq': 52, 'bk': 53, 'bb2': 54, 'bk2': 55, 'br': 56,
#     'bp1': 57, 'bp2': 58, 'bp3': 59, 'bp4': 60, 'bp5': 61, 'bp6': 62, 'bp7': 63, 'bp8': 64}

# field from 0 to 64
field = []
for i in range(1, 65):
    field.append(i)

# all 16 characters
figures = ['wr1', 'wk1', 'wb1', 'wq0', 'wk0', 'wb2', 'wk2', 'wr2',
         'wp1', 'wp2', 'wp3', 'wp4', 'wp5', 'wp6', 'wp7', 'wp8',
         'bp1', 'bp2', 'bp3', 'bp4', 'bp5', 'bp6', 'bp7', 'bp8',
         'br1', 'bk1', 'bb1', 'bq0', 'bk0', 'bb2', 'bk2', 'br2',]

# figures = []
# for i in range(0, 32):
#     figures.append(bin(i))

# board 0-64 with figures
board = []
for i in range(0, 16):
    board.append(figures[i])
for i in range(16, 48):
    board.append('   ')
for i in range(48, 64):
    board.append(figures[i - 32])
    


# function for plotting a chessboard
def plot(board: list) -> None:
    n = 0

    for i in range(0, 17):
        line = ''
        
        if i % 2 == 0: 
            for i in range(0, 33):
                if i % 4 == 0 and i != 32 and i != 0:
                    line = line + '+'
                else:
                    line = line + '-'

        else: 
            for j in range(0, 40):
                if j % 5 == 0: 
                    line = line + '¦' + board[n]
                    n = n + 1
                elif j == 39:
                    line = line + '¦'

        print(line)
    print('\n-- -- -- -- -- -- -- -- -- -- --\n')


# move char xy from a to b
def move_to(board, a, b):
    board[b - 1] = board[a - 1]
    board[a - 1] = '   '


# check if planned move is allowed
def check_move(board, a, b) -> bool:
    # gets figure a and b
    fig_a = board[a - 1]
    fig_b = board[b - 1]

    # checks if goal is same team 
    if fig_a[0] == fig_b[0]:
        return False
    
    # list of allowed per fig? 
    
    # use function from check for this



# move_to(board, 2, 25)
# plot(board)


