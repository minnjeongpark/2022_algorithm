import sys
from pprint import pprint


N, M, K = map(int, sys.stdin.readline().split())

drct = {1: (-1, 0),
      2: (1, 0),
      3: (0, -1),
      4: (0, 1)}

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

tmp = list(map(int, sys.stdin.readline().split()))
shark_d = {i+1:tmp[i] for i in range(M)} # 현재 상어 방향
print(shark_d)
priority = dict()
for i in range(1, M+1):
    tmp = dict()
    for j in range(4):
        tmp[j+1] = list(map(int, sys.stdin.readline().split()))
    priority[i] = tmp
pprint(priority)

trace = [[[] for _ in range(N)] for _ in range(N)] # 상어
# 번호와 흔적


def sol():
    # 먼저 냄새뿌림
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                trace.append([board[i][j], K])

    # 상어이동
    tmp = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j]:

sol()