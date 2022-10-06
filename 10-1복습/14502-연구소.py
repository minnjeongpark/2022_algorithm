import sys
from collections import deque


N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
virus = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            virus.append((i, j))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 0


def pprint(brd):
    for i in range(N):
        print(brd[i][:])


def spread_virus(brd):
    v = [[0]*M for _ in range(N)]
    for vx, vy in virus:
        q = deque()
        q.append((vx, vy))
        v[vx][vy] = 1
        while q:
            x, y = q.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < N and 0 <= ny < M and brd[nx][ny] == 0 and v[nx][ny] == 0:
                    q.append((nx, ny))
                    v[nx][ny] = 1
                    brd[nx][ny] = 2


def count_safe(brd):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if brd[i][j] == 0:
                cnt += 1
    return cnt


def select_wall(start, count):
    global answer, t
    if count == 3:
        tmp = [b[:] for b in board]
        spread_virus(tmp)
        # pprint(tmp)
        tmp_answer = count_safe(tmp)
        answer = max(answer, tmp_answer)
        return
    else:
        for i in range(start, N*M):
            tx = i // M
            ty = i % M
            if board[tx][ty] == 0:
                board[tx][ty] = 1
                select_wall(i, count+1)
                board[tx][ty] = 0

select_wall(0, 0)
print(answer)