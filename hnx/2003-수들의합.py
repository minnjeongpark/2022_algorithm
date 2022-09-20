# 투포인터
import sys


n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

answer = 0
left = 0
right = 1
sum_num = 0

while left <= right and right <= n:
    sum_num = sum(nums[left:right])
    if sum_num == m:
        right += 1
        answer += 1
    elif sum_num < m:
        right += 1
    else:
        left += 1

print(answer)


