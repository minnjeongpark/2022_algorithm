# dfs
nc = int(input())
n = int(input())
network = dict()

for i in range(nc):
    network[i+1] = set()


for _ in range(n):
    x, y = map(int, input().split())
    network[x].add(y)
    network[y].add(x)


v = []


def dfs(start, d):
    for x in d[start]:
        if x not in v:
            v.append(x)
            dfs(x, d)


dfs(1, network)
print(len(v)-1)


from collections import deque

v = []


def bfs(start, d):
    q = deque()
    q.append(start)
    while q:
        x = q.pop()
        for node in d[x]:
            if node not in v:
                v.append(node)
                q.append(node)


bfs(1, network)

print(len(v)-1)
