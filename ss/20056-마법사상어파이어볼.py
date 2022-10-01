import sys

#
# def pprint(x):
#     for xi in range(N):
#         print(x[xi])


N, M, K = map(int, sys.stdin.readline().split())

fbd = {0: (-1, 0),
      1: (-1, 1),
      2: (0, 1),
      3: (1, 1),
      4: (1, 0),
      5: (1, -1),
      6: (0, -1),
      7: (-1, -1)}

board = [[[] for __ in range(N)] for _ in range(N)]


for _ in range(M):
    _r, _c, _m, _s, _d = map(int, sys.stdin.readline().split())
    board[_r-1][_c-1].append([_m, _s, _d])


def move():
    global board
    # 이동
    tmp = [[[] for ___ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                for xx in board[i][j]:
                    nm, ns, nd = xx
                    ni = (i + fbd[nd][0] * ns) % N
                    nj = (j + fbd[nd][1] * ns) % N
                    tmp[ni][nj].append([nm, ns, nd])
    # 파이어볼 나누기
    for i in range(N):
        for j in range(N):
            fb_n = len(tmp[i][j])
            if fb_n > 1:
                # 파이어볼 나누기
                tmp_m, tmp_s, odd, even = 0, 0, 0, 0
                for x in tmp[i][j]:
                    mm, ss, dd = x
                    tmp_m += mm
                    tmp_s += ss
                    if dd % 2:
                        odd += 1
                    else:
                        even += 1
                tmp_m //= 5
                if tmp_m:
                    tmp_s //= fb_n
                    if odd == fb_n or even == fb_n:
                        d = [0, 2, 4, 6]
                    else:
                        d = [1, 3, 5, 7]
                    tmp[i][j] = []
                    for di in d:
                        tmp[i][j].append([tmp_m, tmp_s, di])
                else:
                    tmp[i][j]=[]
    board = tmp


answer = 0
for _ in range(K):
    move()


for i in range(N):
    for j in range(N):
        if board[i][j]:
            for x in board[i][j]:
                answer += x[0]

print(answer)