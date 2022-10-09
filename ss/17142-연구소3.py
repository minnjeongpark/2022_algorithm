import sys
from collections import deque # 바이러스 퍼트릴때는 bfs
from itertools import combinations
from sys import setrecursionlimit
setrecursionlimit(10**6)

import time
start = time.time()

def pprint(b):
    for i in range(N):
        print(b[i])


N, M = map(int, sys.stdin.readline().split())
board = []
virus_pos = []
for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    board.append(tmp)
    for j in range(N):
        if board[i][j] == 2:
            virus_pos.append((i, j))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
min_time = float('inf')
activate_virus = []
max_virus_area = 0

for i in range(N):
    for j in range(N):
        if board[i][j] == 0 or board[i][j] == 2:
            max_virus_area += 1


def count_virus(visited):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] >= 0:
                cnt += 1
    return cnt


def spread_virus(atv_virus):
    v = [[-1]*N for _ in range(N)]
    q = deque()
    answer = 0
    for vx, vy in atv_virus:
        v[vx][vy] = 0
        q.append((vx, vy))

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and v[nx][ny] == -1:
                if board[nx][ny] == 0:
                    q.append((nx, ny))
                    v[nx][ny] = v[x][y] + 1
                    answer = max(answer, v[nx][ny]) # ** 이 과정에서 초(최대값) 찾기
                elif board[nx][ny] == 2:  # 비활성 바이러스 칸
                    q.append((nx, ny))
                    v[nx][ny] = v[x][y] + 1
    virus_area = 0
    for i in range(N):
        for j in range(N):
            if v[i][j] != -1:
                virus_area += 1
    if max_virus_area != virus_area:
        return float('inf')
    return answer

virus_v = [[False]*N for _ in range(N)]


# 무슨 바이러스를 깨울건지 선택
# def select_virus(start, virus_count, tmp_virus_list):
#     global min_time, activate_virus
#     if virus_count == M:
#         # 바이러스 퍼뜨리기
#         tmp_time = spread_virus(tmp_virus_list)
#         if tmp_time == -1:
#             return
#         if 0 <= tmp_time < min_time:
#             activate_virus = tmp_virus_list
#             min_time = tmp_time
#         return
#     else:
#         # for i in range(start, M):
#         #     vp = virus_pos[i]
#         #     if not virus_v[vp[0]][vp[1]]:
#         #         virus_v[vp[0]][vp[1]] = True
#         #         select_virus(start + 1, virus_count + 1, tmp_virus_list + [vp])
#         #         virus_v[vp[0]][vp[1]] = False
#         for vp in virus_pos[start:]:
#             if not virus_v[vp[0]][vp[1]]:
#                 virus_v[vp[0]][vp[1]] = True
#                 select_virus(start+1, virus_count+1, tmp_virus_list + [vp])
#                 virus_v[vp[0]][vp[1]] = False

# select_virus(0, 0, [])
#
virus_combinations = list(combinations(virus_pos, M))
for act_virus in virus_combinations:
    min_time = min(min_time, spread_virus(act_virus))
if min_time == float('inf'):
    print(-1)
else:
    # print(activate_virus)
    print(min_time)
    # print(max_virus_area)

# print("time :", time.time() - start)