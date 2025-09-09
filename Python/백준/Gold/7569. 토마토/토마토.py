import sys
from collections import deque

input = sys.stdin.readline
M, N, H = map(int, input().split())

boxes = []
q = deque()
unripe = 0

for h in range(H):
    layer = []
    for r in range(N):
        row = list(map(int, input().split()))
        layer.append(row)
        for c, v in enumerate(row):
            if v == 1:
                q.append((h, r, c, 0))
            elif v == 0:
                unripe += 1
    boxes.append(layer)

if unripe == 0:
    print(0)
    sys.exit(0)

dz = (1, -1, 0, 0, 0, 0)
dy = (0, 0, 1, -1, 0, 0)
dx = (0, 0, 0, 0, 1, -1)

max_day = 0

while q:
    z, y, x, day = q.popleft()
    for dir in range(6):
        nz = z + dz[dir]
        ny = y + dy[dir]
        nx = x + dx[dir]
        if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
            if boxes[nz][ny][nx] == 0:
                boxes[nz][ny][nx] = 1
                unripe -= 1
                nd = day + 1
                if nd > max_day:
                    max_day = nd
                q.append((nz, ny, nx, nd))

print(-1 if unripe > 0 else max_day)