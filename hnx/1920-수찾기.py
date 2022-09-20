import sys


n = int(sys.stdin.readline())
nums = sorted(list(map(int, sys.stdin.readline().split())))
m = list(map(int, sys.stdin.readline().split()))
target = list(map(int, sys.stdin.readline().split()))


def sol(t):
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == t:
            return mid
        elif nums[mid] > t:
            high = mid - 1
        else:
            low = mid + 1

    return -1


for t in target:
    answer = sol(t)
    if answer == -1:
        print(0)
    else:
        print(1)


