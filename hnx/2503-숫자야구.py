# 완전 탐색
import sys
from itertools import permutations

data = [str(i) for i in range(1, 10)]
candis = list(permutations(data, 3))

n = int(sys.stdin.readline())

for _ in range(n):
    x, s, b = map(int, sys.stdin.readline().split())
    x = list(str(x))
    removes = 0
    for i in range(len(candis)):
        strike = 0
        ball = 0
        i -= removes
        for j in range(3):
            if candis[i][j] == x[j]:
                strike += 1
            elif x[j] in candis[i]:
                ball += 1
        if (strike != s) or (ball != b):
            candis.remove(candis[i])
            removes += 1

print(len(candis))
