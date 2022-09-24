import sys
from pprint import pprint
from collections import deque


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline()[:-1])) for _ in range(n)]

v = [[-1] * m for _ in range(n)]


# sx, sy: 시작 위치
def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    v[sx][sy] = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and v[nx][ny] == -1:
                q.append((nx, ny))
                v[nx][ny] = v[x][y] + 1
                if nx == n-1 and ny == m-1:
                    return


bfs(0, 0)
print(v[n-1][m-1])