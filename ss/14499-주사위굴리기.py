import sys

n, m, x, y, k = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [0, 0, -1, 1] # 동 서 북 남
dy = [1, -1, 0, 0]

# 명령 순서
# 동쪽 1, 서쪽 2, 북쪽 3, 남쪽 4
orders = list(map(int, sys.stdin.readline().split()))


dice = [0]*6 # 윗면, 동쪽, 바닥면, 서쪽, 북쪽, 남쪽
answer = 0


def turn(order):
    if order == 1: # 동쪽
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]
    elif order == 2: #서쪽
        dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]
    elif order == 3: # 북쪽으로굴림 -> 윗면/북쪽/바닥면/남쪽 -> 남쪽/윗면/북쪽/바닥면
        dice[0], dice[4], dice[2], dice[5] = dice[5], dice[0], dice[4], dice[2]
    elif order == 4: # 남쪽으로굴림 -> 윗면/남쪽/바닥면/북쪽 -> 북쪽/윗면/남쪽/바닥면
        dice[0], dice[5], dice[2], dice[4] = dice[4], dice[0], dice[5], dice[2]


nx, ny = x, y
for order in orders:
    nx += dx[order-1]
    ny += dy[order-1]
    if 0 <= nx < n and 0 <= ny < m:
        turn(order)
        if graph[nx][ny] == 0:
            graph[nx][ny] = dice[2]
        else:
            dice[2] = graph[nx][ny]
            graph[nx][ny] = 0
        print(dice[0])
    else:
        nx -= dx[order-1]
        ny -= dy[order-1]