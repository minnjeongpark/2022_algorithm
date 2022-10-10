import sys
from pprint import pprint
# M개의 물고기

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
sdx = [-1, 0, 1, 0]
sdy = [0, -1, 0, 1]

M, S = map(int, sys.stdin.readline().split()) # 물고기 수와 마법 횟수
board = [[[[], []] for _ in range(4)] for _ in range(4)]
for _ in range(M):
    fx, fy, d = map(int, sys.stdin.readline().split())
    board[fx-1][fy-1][0].append(d-1)

# pprint(board)
ssx, ssy = map(int, sys.stdin.readline().split())
ssx -= 1
ssy -= 1

# 1 물고기 복제 -> 5번에 완료됨
def copy_fish():
    global board
    for i in range(4):
        for j in range(4):
            if board[i][j][0]:
                for x in board[i][j][0]:
                    board[i][j][1].append(x)


fish_smell = [[0]*4 for _ in range(4)]


# 2 물고기 이동
def move_fish():
    global board
    new_fish_position = []
    for i in range(4):
        for j in range(4):
            if board[i][j][0]:
                for fish_d in board[i][j][0]:
                    flag = False # 이동햇는지
                    for k in range(8):
                        nfd = (fish_d-k) % 8
                        nx = i + dx[nfd]
                        ny = j + dy[nfd]
                        if 0 <= nx < 4 and 0 <= ny < 4:
                            if not (ssx == nx and ssy == ny) and not fish_smell[nx][ny]:
                                flag = True
                                new_fish_position.append((nx, ny, nfd))
                                break
                    if not flag:
                        new_fish_position.append((i, j, fish_d))
                board[i][j][0] = []
    return new_fish_position


visited = [[0]* 4 for _ in range(4)]
# 3-1 상어 이동 루트 정하기
def select_shark_path(sx, sy, move, fish_count, tmp_path):
    global shark_path, max_fish_count
    if move == 3:
        if fish_count > max_fish_count:
            shark_path = [tp for tp in tmp_path]
            max_fish_count = fish_count
        return
    for d in range(4):
        nsx = sx + sdx[d]
        nsy = sy + sdy[d]
        if 0 <= nsx < 4 and 0 <= nsy < 4:
            if visited[nsx][nsy] == 0:
                visited[nsx][nsy] = 1
                select_shark_path(nsx, nsy, move+1, fish_count + len(board[nsx][nsy][0]), tmp_path+[d])
                visited[nsx][nsy] = 0
            else:
                select_shark_path(nsx, nsy, move+1, fish_count, tmp_path+[d])


def move_shark():
    global ssx, ssy, shark_path
    for nsd in shark_path:
        ssx = ssx + sdx[nsd]
        ssy = ssy + sdy[nsd]
        if board[ssx][ssy][0]:
            board[ssx][ssy][0] = []
            fish_smell[ssx][ssy] = 3

# 4 냄새 줄이기
def remove_smell():
    global fish_smell
    for i in range(4):
        for j in range(4):
            if fish_smell[i][j]:
                fish_smell[i][j] -= 1


def add_copy_fish():
    global board
    for i in range(4):
        for j in range(4):
            if board[i][j][1]:
                for x in board[i][j][1]:
                    board[i][j][0].append(x)
                board[i][j][1] = []


for _ in range(S):
    # 1 복제 마법
    copy_fish()
    # 2 물고기 이동
    new_fish_pos = move_fish()
    for fx, fy, fd in new_fish_pos:
        board[fx][fy][0].append(fd)

    shark_path = []
    max_fish_count = -1
    # 3-1 상어 루트 고르기
    select_shark_path(ssx, ssy, 0, 0, [])
    # 3-2 상어 이동
    move_shark()

    # 4 냄새 줄이기
    remove_smell()

    # 5 복제마법 완료하기
    add_copy_fish()

answer = 0
for i in range(4):
    for j in range(4):
        if board[i][j][0]:
            answer += len(board[i][j][0])

print(answer)