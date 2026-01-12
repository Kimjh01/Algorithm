import sys
r, c = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline().strip()) for _ in range(r)]
new_grid = [row[:] for row in grid]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(r):
    for j in range(c):
        if grid[i][j] == 'X':
            sea_count = 0
            for k in range(4):
                ni, nj = i + dr[k], j + dc[k]
                if 0 <= ni < r and 0 <= nj < c:
                    if grid[ni][nj] == '.':
                        sea_count += 1
                else:
                    sea_count += 1
            if sea_count >= 3:
                new_grid[i][j] = '.'

min_r, max_r, min_c, max_c = r, 0, c, 0
exists = False
for i in range(r):
    for j in range(c):
        if new_grid[i][j] == 'X':
            min_r = min(min_r, i)
            max_r = max(max_r, i)
            min_c = min(min_c, j)
            max_c = max(max_c, j)
            exists = True

if not exists:
    print("X")
else:
    for i in range(min_r, max_r + 1):
        print("".join(new_grid[i][min_c:max_c + 1]))