# calculate the fields left/right from the rook 
if a%8 == 0: 
    L = 0
else: 
    L = (a-1)%8  
R = 7 - L
for i in range(1, L+1):
    allowed.append(-i)
for i in range(1, R+1):
    allowed.append(i)


# calculate the fields above/ beneath  from the rook
U = 0
for i in range(a, 8, -8):
    U = U + 1
D = 7 - U

for i in range(a-64, a+64, 8):
    if i in range(1, 65): 
        allowed.append(i-a)
allowed.remove(0)

left = []
for i in range(-7, 0):
    if i in allowed:
        left.append(i)

right = []
for i in range(1, 8):
    if i in allowed:
        right.append(i)

up = []
for i in range(-8*U -8, 0, 8):
    if i in allowed:
        up.append(i)

down = []
for i in range(0, 8*D, 8):
    if i in allowed:
        down.append(i)

# reset allowed, later add r, l, u, d       
allowed = []

# down check
down_final = []
for i in down: 
    if board[a-1+i] == '   ':
        allowed.append(i)
    elif board[a-1+i][0] == team:
        allowed.append(i)
        break
    elif board[a-1+i][0] ==  enemy: 
        allowed.append(i)
        break

# up check
up_final = []
up.sort(reverse=True)
for i in up: 
    if board[a-1+i] == '   ':
        allowed.append(i)
    elif board[a-1+i][0] == team:
        break
    elif board[a-1+i][0] ==  enemy: 
        allowed.append(i)
        break

# left check
up_final = []
left.sort(reverse=True)
for i in left: 
    if board[a-1+i] == '   ':
        allowed.append(i)
    elif board[a-1+i][0] == team:
        break
    elif board[a-1+i][0] ==  enemy: 
        allowed.append(i)
        break
    
# right check
for i in right: 
    if board[a-1+i] == '   ':
        allowed.append(i)
    elif board[a-1+i][0] == team:
        break
    elif board[a-1+i][0] ==  enemy: 
        allowed.append(i)
        break

allowed.sort()