# 다이나믹 프로그래밍
import sys

# dfs


def sol(x):
    if dp[x] > 0:
        return dp[x]
    if x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3:
        return 4
    else:
        dp[x] = sol(x-1) + sol(x-2) + sol(x-3)
        return dp[x]


n = int(sys.stdin.readline())
for _ in range(n):
    x = int(sys.stdin.readline())
    dp = [0] * (x+1)

    print(sol(x))