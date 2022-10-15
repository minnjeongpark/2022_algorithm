import sys


N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

max_value = 0
v = [[False]*M for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(i, j, cnt, value):
    global max_value, tmp
    if cnt == 4:
        max_value = max(max_value, value)
        return

    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < N and 0 <= ny < M and not v[nx][ny]:
            v[nx][ny] = True
            dfs(nx, ny, cnt+1, value+board[nx][ny])
            v[nx][ny] = False


def combinations(arr, n):
    for i in range(len(arr)):
        if n == 1:
            yield [arr[i]]
        else:
            for next in combinations(arr[i+1:], n-1):
                yield [arr[i]] + next


# ㅗ ㅜ ㅏ ㅓ 처리하기
def mid(x, y):
    global max_value
    candis = combinations([0, 1, 2, 3], 3)
    for candi in candis:
        c1, c2, c3 = candi

        nx1, ny1 = x + dx[c1], y + dy[c1]
        nx2, ny2 = x + dx[c2], y + dy[c2]
        nx3, ny3 = x + dx[c3], y + dy[c3]
        if 0 <= nx1 < N and 0 <= ny1 < M and 0 <= nx2 < N and 0 <= ny2 < M and 0 <= nx3 < N and 0 <= ny3 < M:
            tmp = board[x][y] + board[nx1][ny1] + board[nx2][ny2] + board[nx3][ny3]
            max_value = max(tmp, max_value)

for i in range(N):
    for j in range(M):
        dfs(i, j, 0, 0)
        mid(i, j)

print(max_value)