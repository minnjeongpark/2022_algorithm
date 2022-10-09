import sys
from collections import deque
from pprint import pprint


N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(sx, sy, color):
    q = deque()
    q.append((sx, sy))
    v[sx][sy] = 1
    block_cnt, rainbow_cnt = 1, 0
    blocks = [[sx, sy]] # 좌표
    rainbows = [] # 좌표
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and v[nx][ny] == 0:
                if board[nx][ny] == color:
                    v[nx][ny] = 1
                    q.append((nx, ny))
                    block_cnt += 1
                    blocks.append((nx, ny))
                elif board[nx][ny] == 0: # 무지개블록이라면
                    v[nx][ny] = 1
                    q.append((nx, ny))
                    rainbow_cnt += 1
                    block_cnt += 1
                    rainbows.append((nx, ny))
    # 무지개블록은 방문해제 해준다
    for rx, ry in rainbows:
        v[rx][ry] = 0

    return [block_cnt, rainbow_cnt, blocks, rainbows]


def remove_block(block):
    global board
    for x, y in block:
        board[x][y] = -2 # 구분짓기위함


# 중력
def gravity():
    global board
    for i in range(N-2, -1, -1): # 밑에서부터
        for j in range(N):
            if board[i][j] > -1:
                tmp_i = i
                while True:
                    if 0 <= tmp_i + 1 < N and board[tmp_i+1][j] == -2:
                        board[tmp_i+1][j] = board[tmp_i][j]
                        board[tmp_i][j] = -2
                        tmp_i += 1
                    else:
                        break


# 반시계 회전
def rotation():
    global board
    new_board = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_board[N-1-j][i] = board[i][j]
    board = new_board


score = 0
while True:
    v = [[0]*N for _ in range(N)]
    blocks = []
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0 and not v[i][j]:
                v[i][j] = 1
                block_info = bfs(i, j, board[i][j])
                if block_info[0] >= 2:
                    blocks.append(block_info)
    blocks.sort(reverse=True)
    # 블록 제거 + 점수더하기
    if not blocks:
        break
    remove_block(blocks[0][2])
    remove_block(blocks[0][3])
    score += (blocks[0][0]**2)

    # 중력
    gravity()

    # 반시계 회전
    rotation()

    # 중력
    gravity()

print(score)