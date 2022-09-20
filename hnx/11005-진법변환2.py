import sys
from string import ascii_uppercase


n, b = map(int, sys.stdin.readline().split())

apb = list(ascii_uppercase)
apd = {str(i+10): x for i, x in enumerate(ascii_uppercase)}
for i in range(10):
    apd[str(i)] = str(i)


def sol(x, b):
    answer = []
    while x:
        answer.append(apd[str(x%b)])
        x //= b
    answer = answer[::-1]
    return ''.join(answer)


print(sol(n, b))