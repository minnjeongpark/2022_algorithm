import sys

n = int(sys.stdin.readline())
board = [list(sys.stdin.readline()[:-1]) for _ in range(n)]
answer = 1
# print(board)


def count_candies():
    result = 1
    for i in range(n):
        tmp = 1
        for j in range(n-1):
            if board[i][j] == board[i][j+1]:
                tmp += 1
            else:
                tmp = 1
            if result < tmp:
                result = tmp
        tmp = 1
        for j in range(n-1):
            if board[j][i] == board[j+1][i]:
                tmp += 1
            else:
                tmp = 1
            if result < tmp:
                result = tmp
    return result


for i in range(n):
    for j in range(n):
        # 바로 옆칸
        if j+1 < n:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            tmp = count_candies()
            answer = max(answer, tmp)
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
        if i+1 < n:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            tmp = count_candies()
            answer = max(answer, tmp)
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(answer)