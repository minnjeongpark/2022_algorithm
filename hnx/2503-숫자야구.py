import sys
from itertools import permutations

data = [str(i) for i in range(1, 10)]
candis = list(permutations(data, 3))

n = int(sys.stdin.readline())

for _ in range(n):
    x, s, b = map(int, sys.stdin.readline().split())
    x = list(str(x))
    removes = 0
    l = len(candis)
    for i in range(l):
        strike = 0
        ball = 0
