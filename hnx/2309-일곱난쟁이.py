import sys


dwarfs = []
for _ in range(9):
    dwarfs.append(int(sys.stdin.readline()))

dwarfs.sort()
answer = []
tmp1 = 0
tmp2 = 0
for i in range(9):
    for j in range(i+1, 9):
        if (sum(dwarfs) -(dwarfs[i] + dwarfs[j])) == 100:
            tmp1 = dwarfs[i]
            tmp2 = dwarfs[j]
            break

dwarfs.remove(tmp1)
dwarfs.remove(tmp2)

for x in dwarfs:
    print(x)
