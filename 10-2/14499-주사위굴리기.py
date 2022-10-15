import sys


n, m, x, y, k = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

orders = list(map(int, sys.stdin.readline().split()))
drct = {1: (0, 1), # 동쪽
        2: (0, -1), # 서쪽
        3: (-1, 0), # 북쪽
        4: (1, 0)} # 남쪽

dice = [0, 0, 0, 0, 0, 0] # 윗면, 북쪽, 동쪽, 서쪽, 남쪽, 바닥면


def turn(direction):
    if direction == 1: # 동쪽
        dice[0], dice[2], dice[5], dice[3] = dice[3], dice[0], dice[2], dice[5]
    elif direction == 2:  # 서쪽
        dice[0], dice[3], dice[5], dice[2] = dice[2], dice[0], dice[3], dice[5]
    elif direction == 3:  # 북쪽
        dice[0], dice[1], dice[5], dice[4] = dice[4], dice[0], dice[1], dice[5]
    elif direction == 4: # 남쪽
        dice[0], dice[4], dice[5], dice[1] = dice[1], dice[0], dice[4], dice[5]


s_x, s_y = x, y
for order in orders:
    nx = s_x + drct[order][0]
    ny = s_y + drct[order][1]
    if not (0 <= nx < n and 0 <= ny < m):
        continue
    turn(order)
    if board[nx][ny] == 0:
        board[nx][ny] = dice[5]
    else:
        dice[5] = board[nx][ny]
        board[nx][ny] = 0
    s_x = nx
    s_y = ny
    print(dice[0])