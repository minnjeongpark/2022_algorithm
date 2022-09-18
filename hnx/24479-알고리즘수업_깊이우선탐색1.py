import sys
sys.setrecursionlimit(10**9)


n, m, r = map(int, sys.stdin.readline().split())
graph = [[]*(n+1) for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)


visit = [0]*(n+1)
cnt = 1

def dfs(v):
    global cnt
    visit[v] = cnt
    graph[v].sort()
    for i in graph[v]:
        if visit[i] == 0:
            cnt += 1
            dfs(i)
            

dfs(r)
for i in range(1, n+1):
    print(visit[i])