import sys

n = int(sys.stdin.readline())

result = 0
for i in range(1, n+1):
    x = list(map(int, str(i)))
    result = sum(x) + i
    if result == n:
        print(i)
        break
    elif i == n:
        print(0)
        break
