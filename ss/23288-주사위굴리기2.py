import sys
from collections import deque


n, m, k = map(int, sys.stdin.readline().split())
gph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dice = [1, 2, 3, 4, 5, 6] # 윗면, 북쪽, 동쪽, 서쪽, 남쪽, 바닥면
# 동 남 서 북 (동쪽에서 시계방향으로)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def turn(order):
    if order == 0: # 동쪽: 윗면 동쪽 바닥면 서쪽 -> 서쪽 윗면 동쪽 바닥면
        dice[0], dice[2], dice[5], dice[3] = dice[3], dice[0], dice[2], dice[5]
    elif order == 1: # 남쪽: 윗면 남쪽 바닥면 북쪽 -> 북쪽 윗면 남쪽 바닥면
        dice[0], dice[4], dice[5], dice[1] = dice[1], dice[0], dice[4], dice[5]
    elif order == 2: # 서쪽: 윗면 서쪽 바닥면 동쪽 -> 동쪽 윗면 서쪽 바닥면
        dice[0], dice[3], dice[5], dice[2] = dice[2], dice[0], dice[3], dice[5]
    elif order == 3: # 북쪽: 윗쪽 북쪽 바닥면 남쪽 -> 남쪽 윗면 북쪽 바닥면
        dice[0], dice[1], dice[5], dice[4] = dice[4], dice[0], dice[1], dice[5]


def bfs(sx, sy):
    q = deque()
    v = [[-1]*m for _ in range(n)]
    q.append((sx, sy))
    v[sx][sy] = 1

    while q:
        x, y = q.popleft()
        target = gph[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and v[nx][ny] == -1 and gph[nx][ny] == target:
                q.append((nx, ny))
                v[nx][ny] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if v[i][j] == 1:
                cnt += 1

    return cnt


answer = 0

# 처음 이동 방향은 동쪽
nx, ny = 0, 0
dir = 0

for i in range(k):
    nx += dx[dir]
    ny += dy[dir]
    if not (0 <= nx < n and 0 <= ny < m):
        nx -= dx[dir]
        ny -= dy[dir]
        dir = (dir + 2) % 4
        nx += dx[dir]
        ny += dy[dir]
    turn(dir)
    a = dice[5]
    b = gph[nx][ny]
    if a > b:
        dir = (dir + 1) % 4
    elif a < b:
        dir = (dir - 1) % 4

    c = bfs(nx, ny)
    b = gph[nx][ny]
    answer += (b * c)


print(answer)