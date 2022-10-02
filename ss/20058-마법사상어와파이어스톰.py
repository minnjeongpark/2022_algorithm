import sys
from collections import deque


def pprint(board):
    for x in board:
        print(x)


N, Q = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(2**N)]
magics = list(map(int, sys.stdin.readline().split()))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = 2**N


# 시계방향으로 90도 + 사라짐
def sol(l):
    global board
    new_board = [[0]*n for _ in range(n)]
    ll = 2**l # l=1 -> ll=2
    tmp = [[0] * ll for _ in range(ll)]
    # tmpn = 8 이고 l = 1 -> 4
    # tmpn = 8 이고 l = 2 -> 2
    # tmpn = 8 이고 l = 3 -> 1
    lll = n//ll
    for k in range(lll):
        for kk in range(lll):
            _k = 2**l*k
            _kk = 2**l*kk
            for r in range(ll):
                for c in range(ll):
                    tmp[c][ll-1-r] = board[_k+r][_kk+c]
            for r in range(ll):
                for c in range(ll):
                    new_board[r+_k][c+_kk] = tmp[r][c]

    board = new_board


# 얼음의 양 줄어듦
def sol2():
    global board
    new_board = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                tmp_cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and board[nx][ny]:
                        tmp_cnt += 1
                if tmp_cnt >= 3:
                    new_board[i][j] = board[i][j]
                else:
                    new_board[i][j] = board[i][j] - 1
    board = new_board


def get_maxarea_and_totalice(bb):
    cnt = 0
    answers = []
    v = [[-1]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if bb[i][j]:
                cnt += bb[i][j]
            if bb[i][j] and v[i][j] == -1:
                q = deque()
                q.append((i, j))
                v[i][j] = 1
                answer = 1
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and bb[nx][ny] and v[nx][ny] == -1:
                            q.append((nx, ny))
                            v[nx][ny] = 1
                            answer += 1
                answers.append(answer)
    if not answers:
        return cnt, 0
    return cnt, max(answers)


for q in magics:
    sol(q)
    sol2()

cnt, ans = get_maxarea_and_totalice(board)
print(cnt)
print(ans)