import sys
from collections import deque
import time
start = time.time()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
N, M = map(int, sys.stdin.readline().split())
board = []
virus = []
for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
    for j in range(M):
        if board[i][j] == 2:
            virus.append((i, j))


def get_safe(brd):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if brd[i][j] == 0:
                cnt += 1
    return cnt


def spread_virus(brd):
    v = [[0]*M for _ in range(N)]
    q = deque()
    for vx, vy in virus:
        if v[vx][vy] == 0:
            q.append((vx, vy))
            v[vx][vy] = 1
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < N and 0 <= ny < M and brd[nx][ny] == 0 and v[nx][ny] == 0:
                        q.append((nx, ny))
                        brd[nx][ny] = 2
                        v[nx][ny] = 1



max_safe_area = 0


def select_walls(start, cnt):
    global max_safe_area
    if cnt == 3:
        tmp_board = [b[:] for b in board]
        spread_virus(tmp_board)
        tmp_safe_area = get_safe(tmp_board)
        max_safe_area = max(max_safe_area, tmp_safe_area)
        return
    for x in range(start, N*M):
        r = x // M
        c = x % M
        if board[r][c] == 0:
            board[r][c] = 1
            select_walls(x+1, cnt+1)
            board[r][c] = 0

select_walls(0, 0)
print(max_safe_area)
# print(time.time() - start)