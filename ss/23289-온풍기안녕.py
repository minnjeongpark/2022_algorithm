import sys
from collections import deque


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
R, C, K = map(int, sys.stdin.readline().split())
targets = []
heaters = []
# [현재온도, 현재 지점에 들어온 온도, 현재 지점에 나간 온도]
temperature = [[[0, 0, 0] for _ in range(C)] for _ in range(R)]
v = [[0]*C for _ in range(R)]
visit_num = 0


for i in range(R):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(C):
        if tmp[j] == 5:
            targets.append((i, j))
        elif tmp[j] > 0:
            if tmp[j] == 1:
                d = 1
            elif tmp[j] == 2:
                d = 3
            elif tmp[j] == 3:
                d = 0
            else:
                d = 2
            heaters.append((i, j, d))

W = int(sys.stdin.readline())
walls = [[[False]*4 for _ in range(C)] for _ in range(R)]
for i in range(W):
    x, y, t = map(int, sys.stdin.readline().split())
    x -= 1
    y -= 1
    if t == 0:
        walls[x][y][0] = True
        walls[x-1][y][2] = True
    else:
        walls[x][y][1] = True
        walls[x][y+1][3] = True


def solv():
    answer = 0
    while True:
        spread_heat()
        set_temperature()
        answer += 1
        if check_targets():
            print(answer)
            return
        if answer == 100:
            print(101)
            return


def check_targets():
    for x, y in targets:
        if temperature[x][y][0] < K:
            return False
    return True


def point_validation(x, y, d, flag=True):
    if not (0 <= x < R and 0 <= y < C):
        return False
    elif walls[x][y][d]:
        return False
    elif flag and v[x][y] == visit_num:
        return False
    return True


# 온도 조절 -> 현재온도 += (현재지점에들어온온도-현재지점에나간온도)
def set_temperature():
    global temperature

    for x in range(R):
        for y in range(C):
            if temperature[x][y] == 0:
                continue
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if point_validation(nx, ny, (d+2)%4, False) and temperature[x][y][0] > temperature[nx][ny][0]:
                    temperature[nx][ny][1] += (temperature[x][y][0]-temperature[nx][ny][0]) // 4
                    temperature[x][y][2] += (temperature[x][y][0]-temperature[nx][ny][0]) // 4
    for x in range(R):
        for y in range(C):
            temperature[x][y][0] += (temperature[x][y][1] - temperature[x][y][2])
            temperature[x][y][1] = temperature[x][y][2] = 0
    for x in range(R):
        for y in range(C):
            if x == 0 or y == 0 or x == R-1 or y == C-1:
                if temperature[x][y][0] > 0:
                    temperature[x][y][0] -= 1


def spread_heat():
    global temperature, v, visit_num

    for sx, sy, d in heaters:
        visit_num += 1
        sx += dx[d]
        sy += dy[d]
        q = deque()
        q.append((sx, sy))
        temperature[sx][sy][0] += 5

        for amount in range(4, 0, -1):
            if not q:
                break
            q_len = len(q)
            for idx in range(q_len):
                x, y = q.pop()
                nx = x + dx[d] + dx[(d-1)%4]
                ny = x + dy[d] + dy[(d-1)%4]
                if point_validation(nx, ny, (d+2)%4) and not walls[x][y][(d-1)%4]:
                    temperature[nx][ny][0] += amount
                    v[nx][ny] = visit_num
                    q.append((nx, ny))
                nx = x + dx[d]
                ny = y + dy[d]
                if point_validation(nx, ny, (d+2)%4):
                    temperature[nx][ny][0] += amount
                    v[nx][ny] = visit_num
                    q.append((nx, ny))

                nx = x + dx[d] + dx[(d+1)%4]
                ny = x + dy[d] + dy[(d+1)%4]
                if point_validation(nx, ny, (d+2)%4) and not walls[x][y][(d+1)%4]:
                    temperature[nx][ny][0] += amount
                    v[nx][ny] = visit_num
                    q.append((nx, ny))

solv()