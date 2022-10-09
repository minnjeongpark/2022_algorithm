import sys
from pprint import pprint

# 물고기 수, 상어가 마법을 연습한 횟수
M, S = map(int, sys.stdin.readline().split())
board = [[[[], []] for _ in range(4)] for _ in range(4)] # 현재 물고기 위치, 복사 물고기
for _ in range(M):
    fx, fy, d = map(int, sys.stdin.readline().split())
    board[fx-1][fy-1][0].append(d-1)
sx, sy = map(int, sys.stdin.readline().split())
sx -= 1
sy -= 1
# 물고기 이동 방향
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
# 상어 이동 방향
sdx = [-1, 0, 1, 0]
sdy = [0, -1, 0, 1]


# 1 복제 마법 -> 5 번 때 칸에 추가함
def copy_fish():
    global board
    for i in range(4):
        for j in range(4):
            if board[i][j][0]:
                for cfd in board[i][j][0]:
                    board[i][j][1].append(cfd)


# 2 물고기 이동
def move_fish():
    global board, fish_smell
    new_fish_position = []
    for i in range(4):
        for j in range(4):
            if board[i][j][0]:
                for fish_d in board[i][j][0]:
                    flag = False
                    for k in range(8):
                        nd = (fish_d - k) % 8
                        nx = i + dx[nd]
                        ny = j + dy[nd]
                        if 0 <= nx < 4 and 0 <= ny < 4:
                            # 상어가 있는 칸도 아니고 물고기 냄새 칸도 아닌
                            if not (nx == sx and ny == sy) and not fish_smell[nx][ny]:
                                new_fish_position.append((nx, ny, nd))
                                flag = True
                                break
                    if not flag:
                        new_fish_position.append((i, j, fish_d))
                board[i][j][0] = []
    return new_fish_position


max_fish_count = -1
shark_route = []
visited = [[False]*4 for _ in range(4)]


# 3-1 상어 루트 정하기
def select_shark_path(shark_x, shark_y, move_count, fish_count, temp_path):
    global board, max_fish_count, shark_route
    if move_count == 3:
        if fish_count > max_fish_count:
            shark_route = [tp for tp in temp_path]
            max_fish_count = fish_count
        return
    for d in range(4):
        nx = shark_x + sdx[d]
        ny = shark_y + sdy[d]
        if 0 <= nx < 4 and 0 <= ny < 4:
            # visited 가 필요한 이유는 fish_count 에 물고기 개수 추가할 때 중복을 막기위함
            if not visited[nx][ny]:
                visited[nx][ny] = True
                select_shark_path(nx, ny, move_count+1, fish_count+len(board[nx][ny][0]), temp_path+[d])
                visited[nx][ny] = False
            else:
                select_shark_path(nx, ny, move_count+1, fish_count, temp_path+[d])


# 3-2 상어 이동 & 물고기 흔적 추가
def move_shark():
    global board, shark_route, sx, sy, fish_smell
    for d in shark_route:
        sx += sdx[d]
        sy += sdy[d]
        if board[sx][sy][0]:
            board[sx][sy][0] = []
            fish_smell[sx][sy] = 3


# 4 냄새 제거 -1
def reduce_fish_smell():
    global fish_smell
    for i in range(4):
        for j in range(4):
            if fish_smell[i][j]:
                fish_smell[i][j] -= 1


# 5 복제 마법 완료하기
def add_copy_fish():
    global board
    for i in range(4):
        for j in range(4):
            if board[i][j][1]:
                for fish in board[i][j][1]:
                    board[i][j][0].append(fish)
                board[i][j][1] = []


fish_smell = [[0]*4 for _ in range(4)]

for __ in range(S):
    # 물고기 복사
    copy_fish()
    # 물고기 이동
    fish_position = move_fish()
    for x, y, d in fish_position:
        board[x][y][0].append(d)

    shark_route = []
    max_fish_count = -1

    select_shark_path(sx, sy, 0, 0, [])
    move_shark()

    reduce_fish_smell()
    add_copy_fish()

result = 0
for i in range(4):
    for j in range(4):
        if board[i][j][0]:
            result += len(board[i][j][0])
print(result)
