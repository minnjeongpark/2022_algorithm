# 완전 탐색
import sys
n = int(sys.stdin.readline())
board = [list(sys.stdin.readline()) for _ in range(n)]

def count_candies(board):
    answer = 1
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if board[i][j] == board[i][j-1]:
                cnt += 1
            else:
                cnt = 1

            if cnt > answer:
                answer = cnt
        cnt = 1
        for j in range(1, n):
            if board[j][i] == board[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            if cnt > answer:
                answer = cnt
    return answer

answer = 0

for i in range(n):
    for j in range(n):
        if j + 1 < n:
            # 인접한 것과 바꾸기
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            tmp = count_candies(board)
            if tmp > answer:
                answer = tmp
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        if i + 1 < n:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            tmp = count_candies(board)
            if tmp > answer:
                answer = tmp
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
print(answer)