# 완전 탐색
import sys

n = int(sys.stdin.readline())

result = 0
for i in range(1, n+1):
    x = list(map(int, str(i)))
    result = i + sum(x)
    if result == n:
        print(i)
        break

    if i == n:
        print(0)