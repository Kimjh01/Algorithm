import sys
input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

zx, zy = -1, -1
for i in range(N):
    for j in range(N):
        if grid[i][j] == 0:
            zx, zy = i, j
            break

target = 0
if zx == 0:
    target = sum(grid[1])
else:
    target = sum(grid[0])

m = target - sum(grid[zx])
grid[zx][zy] = m

if m <= 0:
    print(-1)
    sys.exit()

possible = True

for i in range(N):
    if sum(grid[i]) != target:
        possible = False
        break

if possible:
    for j in range(N):
        col_sum = 0
        for i in range(N):
            col_sum += grid[i][j]
        if col_sum != target:
            possible = False
            break

if possible:
    d1 = 0
    d2 = 0
    for i in range(N):
        d1 += grid[i][i]
        d2 += grid[i][N - 1 - i]
    if d1 != target or d2 != target:
        possible = False

if possible:
    print(m)
else:
    print(-1)