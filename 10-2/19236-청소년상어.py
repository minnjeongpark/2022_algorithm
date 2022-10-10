import sys

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
bboard = [[[] for _ in range(4)] for _ in range(4)]
for i in range(4):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(4):
        a, b = tmp[j*2], tmp[j*2+1]
        bboard[i][j] = [a, b-1]

from pprint import pprint
pprint(bboard)

answer = 0


def sol(sx, sy, score, board):
    global answer
    score += board[sx][sy][0]
    answer = max(answer, score)
    board[sx][sy][0] = 0
    sd = board[sx][sy][1]

    for fish_num in range(1, 17):
        fx, fy = -1, -1
        for i in range(4):
            for j in range(4):
                if board[i][j][0] == fish_num:
                    # 빈칸, ㄷ른 물고기가 있는 칸으로 이동가능,
                    # 상어칸, 공간의 경계 이동불가능
                    fx, fy = i, j
        if fx == -1 and fy == -1:
            continue
        fd = board[fx][fy][1]
        for k in range(8):
            nfd = (fd + k) % 8
            nx = fx + dx[nfd]
            ny = fy + dy[nfd]
            if 0 <= nx < 4 and 0 <= ny < 4 and not (sx == nx and sy == ny):
                board[fx][fy][1] = nfd
                board[fx][fy], board[nx][ny] = board[nx][ny], board[fx][fy]
                break
    # 상어이동
    for k in range(1, 5):
        nsx = sx + dx[sd]*k
        nsy = sy + dy[sd]*k
        if 0 <= nsx < 4 and 0 <= nsy < 4 and board[nsx][nsy][0] > 0:
            tmp_board = []
            for i in range(4):
                ttmp = []
                for j in range(4):
                    ttmp.append(board[i][j][:])
                tmp_board.append(ttmp)
            sol(nsx, nsy, score, tmp_board)

sol(0, 0, 0, bboard)
print(answer)