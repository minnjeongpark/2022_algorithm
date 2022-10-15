import sys
from pprint import pprint

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
sdx = [-1, 0, 1, 0]
sdy = [0, -1, 0, 1]
board = [[[[], []] for _ in range(4)] for _ in range(4)]


M, S = map(int, sys.stdin.readline().split())
for _ in range(M):
    fx, fy, d = map(int, sys.stdin.readline().split())
    board[fx-1][fy-1][0].append(d-1)
ssx, ssy = map(int, sys.stdin.readline().split())
ssx -= 1
ssy -= 1


fish_smell = [[0]*4 for _ in range(4)]


# 1 물고기 복제
def copy_fish():
    global board
    for i in range(4):
        for j in range(4):
            if board[i][j][0]:
                for fish in board[i][j][0]:
                    board[i][j][1].append(fish)


# 2 물고기 이동
def move_fish():
    global board
    fish_position = []
    for i in range(4):
        for j in range(4):
            if board[i][j][0]:
                for fish_d in board[i][j][0]:
                    flag = False
                    for k in range(8):
                        n_d = (fish_d - k) % 8
                        nx = i + dx[n_d]
                        ny = j + dy[n_d]
                        if 0 <= nx < 4 and 0 <= ny < 4 and not (nx == ssx and ny == ssy) and fish_smell[nx][ny] == 0:
                            fish_position.append((nx, ny, n_d))
                            flag = True
                            break
                    if not flag:
                        fish_position.append((i, j, fish_d))
                board[i][j][0] = []
    return fish_position


# 3 상어이동
# 3-1 상어 경로 정하기
def select_shark_route(sx, sy, cnt, fish_num, tmp_shark_route):
    global max_fish, shark_route, v
    if cnt == 3:
        if fish_num > max_fish:
            max_fish = fish_num
            shark_route = tmp_shark_route
        return

    for k in range(4):
        nsx = sx + sdx[k]
        nsy = sy + sdy[k]
        if 0 <= nsx < 4 and 0 <= nsy < 4:
            if not v[nsx][nsy]:
                v[nsx][nsy] = True
                select_shark_route(nsx, nsy, cnt+1, fish_num+len(board[nsx][nsy][0]), tmp_shark_route+[k])
                v[nsx][nsy] = False
            else:
                select_shark_route(nsx, nsy, cnt+1, fish_num, tmp_shark_route+[k])


# 3-2 상어이동
def move_shark():
    global fish_smell, shark_route, ssx, ssy, board
    for d in shark_route:
        ssx += sdx[d]
        ssy += sdy[d]
        if board[ssx][ssy][0]:
            board[ssx][ssy][0] = []
            fish_smell[ssx][ssy] = 3


# 4 물고기 냄새 제거
def remove_fish_smell():
    global board, fish_smell
    for i in range(4):
        for j in range(4):
            if fish_smell[i][j]:
                fish_smell[i][j] -= 1


# 5 복제마법 완료
def add_copy_fish():
    for i in range(4):
        for j in range(4):
            if board[i][j][1]:
                for fish in board[i][j][1]:
                    board[i][j][0].append(fish)
                board[i][j][1] = []


for _ in range(S):
    # 1
    copy_fish()
    # 2
    new_fish_position = move_fish()

    for fx, fy, d in new_fish_position:
        board[fx][fy][0].append(d)

    shark_route = []
    max_fish = -1
    v = [[False]*4 for _ in range(4)]
    # 3
    select_shark_route(ssx, ssy, 0, 0, [])
    move_shark()

    # 4
    remove_fish_smell()

    # 5
    add_copy_fish()

answer = 0
for i in range(4):
    for j in range(4):
        if board[i][j][0]:
            answer += len(board[i][j][0])

print(answer)