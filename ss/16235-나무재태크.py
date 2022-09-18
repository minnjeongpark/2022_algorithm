import sys

ds = [(-1, -1), (-1, 0), (-1, 1),
      (0, -1), (0, 1),
      (1, -1), (1, 0), (1, 1)]

n, m, K = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
trees = [[[] for __ in range(n)] for _ in range(n)]
a = [[5]*n for _ in range(n)]
for _ in range(m):
    x, y, age = map(int, sys.stdin.readline().split())
    trees[x-1][y-1].append(age)


for k in range(K):
    for i in range(n):
        for j in range(n):
            if trees[i][j]:
                trees[i][j].sort()
                tmp_tree = []
                dead_tree = 0
                for age in trees[i][j]:
                    if age <= a[i][j]:
                        a[i][j] -= age
                        age += 1
                        tmp_tree.append(age)
                    else:
                        dead_tree += age // 2
                trees[i][j] = tmp_tree
                a[i][j] += dead_tree
    if not trees:
        print(0)
        sys.exit(0)
    for i in range(n):
        for j in range(n):
            if trees[i][j]:
                for age in trees[i][j]:
                    if age % 5 == 0:
                        for d in ds:
                            nx = i + d[0]
                            ny = j + d[1]
                            if 0 <= nx < n and 0 <= ny < n:
                                trees[nx][ny].append(1)

    for i in range(n):
        for j in range(n):
            a[i][j] += board[i][j]


answer = 0
for i in range(n):
    for j in range(n):
        answer += len(trees[i][j])
print(answer)