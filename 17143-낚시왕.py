import sys
from pprint import pprint


R, C, M = map(int, sys.stdin.readline().split())
board = [[[]for __ in range(C)] for _ in range(R)]

# d가 1: 위, 2: 아래, 3: 오른쪽, 4: 왼쪽
ds = {1: (-1, 0), 2: (1, 0), 3: (0, 1), 4: (0, -1)}


for _ in range(M):
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    board[r-1][c-1].append([s, d, z]) # 속력, 이동방향, 크기

answer = 0


# 낚시왕의 열에 있는 상어
def get_dist(shk_y):
    global answer
    for i in range(R):
        if board[i][shk_y]:
            answer += board[i][shk_y][0][2]
            board[i][shk_y] = []
            return


def get_next_pos(x, y, speed, direction):
    if direction == 1 or direction == 2:
        speed %= ((R-1)*2)
    if direction == 3 or direction == 4:
        speed %= ((C-1)*2)
    while speed:
        dx, dy = ds[direction]
        nx = x + dx
        ny = y + dy
        if 0 <= nx < R and 0 <= ny < C:
            x = nx
            y = ny
            speed -= 1
        else:
            if direction == 1 or direction == 3:
                direction += 1
            elif direction == 2 or direction == 4:
                direction -= 1
    return x, y, direction


def shark_move():
    global board
    new_board = [[[] for __ in range(C)] for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if board[i][j]:
                ni, nj, nd = get_next_pos(i, j, board[i][j][0][0], board[i][j][0][1])
                new_board[ni][nj].append([board[i][j][0][0], nd, board[i][j][0][2]])

    board = new_board


for j in range(C):
    get_dist(j)
    shark_move()
    for x in range(R):
        for y in range(C):
            if board[x][y]:
                board[x][y].sort(key=lambda k: k[2], reverse=True)
                board[x][y] = [board[x][y][0]]
print(answer)

