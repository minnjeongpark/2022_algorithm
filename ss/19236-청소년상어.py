import copy
import sys


bboard = [[] for _ in range(4)]

for i in range(4):
    tmp = list(map(int, sys.stdin.readline().split()))
    fish = []
    for j in range(4):
        a = tmp[j*2]
        b = tmp[j*2+1]-1
        fish.append([a, b])
    bboard[i] = fish

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

answer = 0


def sol(sx, sy, score, board):
    global answer
    score += board[sx][sy][0]
    answer = max(answer, score)
    board[sx][sy][0] = 0

    # 물고기 이동
    for fn in range(1, 17):
        fx, fy = -1, -1
        for i in range(4):
            for j in range(4):
                if board[i][j][0] == fn:
                    fx, fy = i, j
                    break

        if fx == -1 and fy == -1:
            continue
        fd = board[fx][fy][1]

        for k in range(8):
            nd = (fd+k) % 8
            nx = fx + dx[nd]
            ny = fy + dy[nd]
            if (0 <= nx < 4 and 0 <= ny < 4) and not (nx == sx and ny == sy):
                board[fx][fy][1] = nd
                board[fx][fy], board[nx][ny] = board[nx][ny], board[fx][fy]
                break
    # 상어 이동
    sd = board[sx][sy][1]
    for k in range(1, 5):
        nsx = sx + dx[sd]*k
        nsy = sy + dy[sd]*k
        if 0 <= nsx < 4 and 0 <= nsy < 4 and board[nsx][nsy][0] > 0:
            tmp = []
            for i in range(4):
                ttmp = []
                for j in range(4):
                    ttmp.append(board[i][j][:])
                tmp.append(ttmp)
            # sol(nsx, nsy, score, copy.deepcopy(board))
            sol(nsx, nsy, score, tmp)


sol(0, 0, 0, bboard)
print(answer)
