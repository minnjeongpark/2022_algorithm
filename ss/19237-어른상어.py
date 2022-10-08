import sys
from pprint import pprint


N, M, K = map(int, sys.stdin.readline().split())
# 위 아래 왼쪽 오른쪽
drct = {1: (-1, 0),
        2: (1, 0),
        3: (0, -1),
        4: (0, 1)}

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
shark = dict()
# 상어 번호와 흔적
graph = [[[] for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if board[i][j]:
            shark[board[i][j]] = [i, j]
            graph[i][j] = [board[i][j], K]


# 현재 상어의 방향
sd = list(map(int, sys.stdin.readline().split()))
for k in range(M):
    shark[k+1].append(sd[k]) # 상어 방향

# 각 상어의 방향 우선순위
# 첫번째 줄: 해당 상어가 위를 향할 때의 방향 우선순위
# 두번째 줄: 해당 상어가 아래를 향할 때의 방향 우선순위
# 세번째 줄: 해당 상어가 왼쪽 향할 때의 방향 우선순위
# 네번째 줄: 해당 상어가 오른쪽 향할 때의 방향 우선순위

priority = dict()
for i in range(M):
    priority[i+1] = dict()
    for j in range(4):
        tmp = list(map(int, sys.stdin.readline().split()))
        priority[i+1][j+1] = tmp


def sol():
    global shark
    cnt = 0
    while True:
        cnt += 1
        # 1번만 남도록 체크
        if cnt > 1000:
            print(-1)
            break
        # 냄새 뿌림
        for s in shark:
            x, y, dd = shark[s]
            graph[x][y] = [s, K]
        # 상어의 이동
        # 새로운 위치에서 상어가 여러마리라면
        # 흔적 처리

        tmp = [[[] for _ in range(N)] for _ in range(N)]
        for s in shark:
            # 상어의 위치와 방향
            sx, sy, sd = shark[s]
            # 현재 방향에 따른 방향 우선순위
            tmp_sd = priority[s][sd] # ex)[3,2,1,4]
            # 이동. 이동 후에 한 칸에 여러마리가 있다면 제일 낮은 번호 상어만 남기기
            flag = False
            for dd in tmp_sd:
                nsx = sx + drct[dd][0]
                nsy = sy + drct[dd][1]
                if 0 <= nsx < N and 0 <= nsy < N:
                    # 이동할 위치에 아무 냄새가 없는 칸
                    if not graph[nsx][nsy]:
                        if tmp[nsx][nsy] and tmp[nsx][nsy][0] > s:
                            # 현재 상어가 이김
                            tmp[nsx][nsy] = [s, dd]
                        elif not tmp[nsx][nsy]:
                            tmp[nsx][nsy] = [s, dd]
                        flag = True
                        break
            if not flag:
                for dd in tmp_sd:
                    nsx = sx + drct[dd][0]
                    nsy = sy + drct[dd][1]
                    if 0 <= nsx < N and 0 <= nsy < N:
                        # 없으면 자신의 냄새가 있는 칸
                        if graph[nsx][nsy] and graph[nsx][nsy][0] == s:
                            # 이미 있으면 비교해서 제거
                            if tmp[nsx][nsy] and tmp[nsx][nsy][0] > s:
                                # 현재 상어가 이김
                                tmp[nsx][nsy] = [s, dd]
                            elif not tmp[nsx][nsy]:
                                tmp[nsx][nsy] = [s, dd]
                            break

        # tmp[i][j] = [상어번호, 상어 방향]
        tmp_shark = dict()
        # 겹치면 상어 제거하기 + 흔적 지워주기 + 합쳐주기 dictation update
        for i in range(N):
            for j in range(N):
                if graph[i][j]:
                    graph[i][j][1] -= 1
                    if graph[i][j][1] == 0:
                        graph[i][j] = []
                if tmp[i][j]:
                    tmp_shark[tmp[i][j][0]] = [i, j, tmp[i][j][1]]
        shark = tmp_shark

        if len(shark) == 1:
            print(cnt)
            break
sol()
