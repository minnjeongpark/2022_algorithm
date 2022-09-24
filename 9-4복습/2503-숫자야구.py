import sys
from itertools import permutations

ns = [str(i) for i in range(1, 10)]
candi = list(permutations(ns, 3))


n = int(sys.stdin.readline())
for _ in range(n):
    tmp, s, b = map(int, sys.stdin.readline().split())
    tmp = list(str(tmp))
    removes = 0
    for i in range(len(candi)):
        strike = 0
        ball = 0
        i -= removes
        for k in range(3):
            if tmp[k] == candi[i][k]:
                strike += 1
            elif tmp[k] in candi[i]:
                ball += 1
        if strike != s or ball != b:
            candi.remove(candi[i])
            removes += 1

print(len(candi))