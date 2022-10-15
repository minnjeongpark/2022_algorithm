import sys


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
N = int(sys.stdin.readline())
n = N*N
board = [[0]*N for _ in range(N)]
students = {}
for ss in range(n):
    student = list(map(int, sys.stdin.readline().split()))
    s = student[0]
    like = student[1:]
    students[s] = like
    if ss == 0:
        board[1][1] = s
        continue

    tmp = []
    for i in range(N):
        for j in range(N):
            like_num, empty_num = 0, 0
            if board[i][j] == 0:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if board[nx][ny] in like:
                            like_num += 1
                        if board[nx][ny] == 0:
                            empty_num += 1
                tmp.append((i, j, like_num, empty_num))
    tmp.sort(key=lambda x: (-x[2], -x[3], x[0]))

    board[tmp[0][0]][tmp[0][1]] = s


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