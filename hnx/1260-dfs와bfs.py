import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1

v1 = [0]*(n+1)
v2 = [0]*(n+1)


def dfs(start):
    v2[start] = 1
    print(start, end=" ")
    for i in range(1, n+1):
        if v2[i] == 0 and graph[start][i]:
            dfs(i)


def bfs(start):
    q = deque()
    q.append(start)
    v1[start] = 1
    while q:
        x = q.popleft()
        print(x, end=" ")
        for i in range(1, n+1):
            if v1[i] == 0 and graph[x][i] == 1:
                q.append(i)
                v1[i] = 1

dfs(v)
print()
bfs(v)