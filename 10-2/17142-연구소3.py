import sys
from collections import deque
from pprint import pprint


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
N, M = map(int, sys.stdin.readline().split())
board = []
virus = []
max_virus_area = 0
for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
    for j in range(N):
        if board[i][j] == 2:
            virus.append((i, j))
            max_virus_area += 1
        if board[i][j] == 0:
            max_virus_area += 1


def get_virus_area(brd):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if brd[i][j] == 2:
                cnt += 1
    return cnt


def combinations(arr, n):
    result = []
    if n == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        rest_arr = arr[i+1:]
        for c in combinations(rest_arr, n-1):
            result.append([elem]+c)

    return result


activate_virus = combinations(virus, M)
# print(activate_virus)

def spread_virus(act_virus, brd):
    global min_time
    q = deque()
    v = [[-1]*N for _ in range(N)]
    for vx, vy in act_virus:
        q.append((vx, vy))
        v[vx][vy] = 0
    tmp_min_time = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and v[nx][ny] == -1:
                # 빈 칸 이라면
                if brd[nx][ny] == 0:
                    brd[nx][ny] = 2
                    q.append((nx, ny))
                    v[nx][ny] = v[x][y] + 1
                    tmp_min_time = max(tmp_min_time, v[nx][ny])
                # 비활성화된 바이러스라면
                if brd[nx][ny] == 2:
                    q.append((nx, ny))
                    v[nx][ny] = v[x][y] + 1

    virus_area = get_virus_area(brd)
    if virus_area != max_virus_area:
        return
    min_time = min(min_time, tmp_min_time)

min_time = float('inf')
for act_virus in activate_virus:
    tmp_board = [b[:] for b in board]
    spread_virus(act_virus, tmp_board)
if min_time == float('inf'):
    print(-1)
else:
    print(min_time)