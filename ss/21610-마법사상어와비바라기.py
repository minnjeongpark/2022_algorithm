import sys

# d 값 받아들이고 -1 해주어야함
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def get_pos(p, d, s):
    return ((p[0]+dx[d-1]*s)%N, (p[1]+dy[d-1]*s)%N)


ps = [(N-2, 0), (N-2, 1), (N-1, 0), (N-1, 1)]
for _ in range(M):
    v = [[-1]*N for _ in range(N)]
    d, s = map(int, sys.stdin.readline().split())
    ll = len(ps)
    for i in range(ll):
        ps[i] = get_pos(ps[i], d, s)
    total_water = 0
    # 구름에 비 1 씩 내리고 구름 사라짐
    for i in range(ll):
        x, y = ps[i]
        v[x][y] = 1
        board[x][y] += 1

    # 물복사 버그, 대각선 물 증가
    for i in range(ll):
        x, y = ps[i]
        cnt = 0
        for _dc in dc:
            nx = x + _dc[0]
            ny = y + _dc[1]
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny]:
                cnt += 1
        board[x][y] += cnt

    # 구름
    tmp_ps = []
    for i in range(N):
        for j in range(N):
            if v[i][j] == -1 and board[i][j] >= 2:
                tmp_ps.append((i, j))
                board[i][j] -= 2
    ps = tmp_ps


answer = 0
for i in range(N):
    for j in range(N):
        answer += board[i][j]
print(answer)