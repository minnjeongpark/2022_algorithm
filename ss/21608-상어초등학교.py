import sys


N = int(sys.stdin.readline())
students = {i: [] for i in range(1, N*N+1)}
board = [[0]*N for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for I in range(N*N):
    tmp_ = list(map(int, sys.stdin.readline().split()))
    sdt = tmp_[0]
    like = tmp_[1:]
    students[sdt] = like
    if I == 0:
        board[1][1] = sdt # 첫번째 학생은 무조건 (1, 1)에 위치
        continue
    tmp = []
    for i in range(N):
        for j in range(N):
            sum_like, sum_empty = 0, 0
            if board[i][j] == 0:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if board[nx][ny] in like:
                            sum_like += 1
                        if board[nx][ny] == 0:
                            sum_empty += 1
                tmp.append((sum_like, sum_empty, i, j))
    tmp.sort(key=lambda x:(-x[0], -x[1], x[2]))

    board[tmp[0][2]][tmp[0][3]] = sdt


answer = 0

for i in range(N):
    for j in range(N):
        fav = 0
        sdt = board[i][j]
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] in students[sdt]:
                    fav += 1
                    continue
        if fav != 0:
            answer += (10**(fav-1))

print(answer)