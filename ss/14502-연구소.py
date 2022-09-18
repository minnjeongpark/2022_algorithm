import sys

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

virus_pos = []
max_safe = 0


for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            virus_pos.append((i, j))


def get_safe(graph):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                cnt += 1

    return cnt


def spread(vx, vy, graph):
    if graph[vx][vy] == 2:
        for k in range(4):
            nx = vx + dx[k]
            ny = vy + dy[k]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = 2
                spread(nx, ny, graph)


def select_wall(start, cnt):
    global max_safe
    if cnt == 3:
        tmp_graph = [b[:] for b in board]
        for vx, vy in virus_pos:
            spread(vx, vy, tmp_graph)
        safe_cnt = get_safe(tmp_graph)
        max_safe = max(max_safe, safe_cnt)
        return
    else:
        for i in range(start, n*m):
            r = i // m
            c = i % m
            if board[r][c] == 0:
                board[r][c] = 1
                select_wall(i, cnt+1)
                board[r][c] = 0

select_wall(0, 0)
print(max_safe)
