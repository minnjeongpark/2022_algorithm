import sys
from collections import deque


n, l, r = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

union = []
v = [[-1]*n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
day = 0


def sol(i, j):
    q = deque()
    q.append((i, j))
    tmp_union = [(i, j)]
    v[i][j] = 1
    pln = board[i][j]
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and v[nx][ny] == -1:
                if l <= abs(board[x][y] - board[nx][ny]) <= r:
                    q.append((nx, ny))
                    v[nx][ny] = 1
                    tmp_union.append((nx, ny))
                    pln += board[nx][ny]
    plnmv = int(pln / len(tmp_union))
    for xx, yy in tmp_union:
        board[xx][yy] = plnmv
    return len(tmp_union)


while True:
    v = [[-1] * n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if v[i][j] == -1:
                if sol(i, j) > 1:
                    flag = True
    if not flag:
        break
    day += 1


print(day)


