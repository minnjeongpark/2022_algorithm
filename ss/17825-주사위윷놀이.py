import sys

# 10, 20, 30 안 지나치는 경로
board1 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]
# 10 만나는 경로
board2 = [0, 2, 4, 6, 8, 10, 13, 16, 19, 25, 30, 35, 40] # 10
# 20 만나는 경로
board3 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 25, 30, 35, 40] # 20
# 30 만나는 경로
board4 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 28, 27, 26, 25, 30, 35, 40]

board = [board1, board2, board3, board4]


answer = 0

def dfs(save_horse, command, idx, score):
    global answer
    if idx == 10:
        answer = max(answer, score)
        return

    for h in range(4):
        if save_horse[h][0] == -1:
            continue
        save_horse[h][1] += command[idx]