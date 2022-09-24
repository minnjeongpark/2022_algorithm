import sys
from collections import deque
from pprint import pprint

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline()[:-1])) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# v[x][y][0] 벽을 뚫지 않고 온 경우의 최단경로
# v[x][y][1] 벽을 뚫지 온 경우의 최단경로


def bfs():
    q = deque()
    q.append((0, 0, 0))
    v = [[[0, 0] for _ in range(m)] for __ in range(n)]
    v[0][0][0] = 1
    while q:
        x, y, w = q.popleft()
        if x == n-1 and y == m-1:
            return v[x][y][w]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                # 다음 이동할 곳이 벽이고 여태 벽 부수기를 안했다면
                if board[nx][ny] == 1 and w == 0:
                    v[nx][ny][1] = v[x][y][0] + 1
                    q.append((nx, ny, 1))
                # 다음 이동할 곳이 벽이 아니고 아직 한번도 방문하지 않았다면
                elif board[nx][ny] == 0 and v[nx][ny][w] == 0:
                    v[nx][ny][w] = v[x][y][w] + 1
                    q.append((nx, ny, w))
    return -1


print(bfs())


# 아래는 시간초과 발생 코드
shortest = float('inf')
# def bfs(sx, sy):
#     q = deque()
#     q.append((sx, sy))
#     v = [[-1]*m for _ in range(n)]
#     v[sx][sy] = 1
#     while q:
#         x, y = q.popleft()
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0 and v[nx][ny] == -1:
#                 q.append((nx, ny))
#                 v[nx][ny] = v[x][y] + 1
#     return v[n-1][m-1]
#
#
# def select_wall(cnt):
#     global shortest
#     if cnt == 1:
#         tmp = bfs(0, 0)
#         if tmp != -1:
#             shortest = min(shortest, tmp)
#         return
#     else:
#         for i in range(n):
#             for j in range(m):
#                 if board[i][j] == 1:
#                     board[i][j] = 0
#                     select_wall(cnt+1)
#                     board[i][j] = 1
#
# select_wall(0)
#
# print(shortest)