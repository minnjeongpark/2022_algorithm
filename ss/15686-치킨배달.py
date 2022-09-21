import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())

def get_dist(h, c):
    return abs(h[0]-c[0]) + abs(h[1]-c[1])


cities = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
chicken = []
home = []
for i in range(n):
    for j in range(n):
        if cities[i][j] == 2:
            chicken.append((i, j))
        elif cities[i][j] == 1:
            home.append((i, j))

candi_chkn = list(combinations(chicken, m))

answer = float('inf')
for cc in candi_chkn: # m개의 치킨집
    tmp = 0
    # m개의 치킨 집 중 하나의 치킨집과 집 사이의 거리 구하기
    for h in home:
        x = 9999
        for i in range(m):
             x = min(x, get_dist(h, cc[i]))
        tmp += x
    answer = min(answer, tmp)

print(answer)