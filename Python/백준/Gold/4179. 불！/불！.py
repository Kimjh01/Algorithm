import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]
INF = float("INF")
fire_time = [[INF] * C for _ in range(R)]
dist = [[-1]*C for _ in range(R)]

ck = False
fq = deque()
jq = deque()

for r in range(R):
    for c in range(C):
        if grid[r][c] == 'F':
            fire_time[r][c] = 0
            fq.append((r, c))
        elif grid[r][c] == 'J':
            jr, jc = r, c

DIR = [(-1,0),(1,0),(0,-1),(0,1)]
while fq:
    r, c = fq.popleft()
    for dr, dc in DIR:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '#' and fire_time[nr][nc] == INF:
            fire_time[nr][nc] = fire_time[r][c] + 1
            fq.append((nr, nc))

dist[jr][jc] = 0
jq.append((jr, jc))
while jq:
    r, c = jq.popleft()
    if r == 0 or r == R-1 or c == 0 or c == C-1:
        print(dist[r][c] + 1)
        ck = True
        break
    for dr, dc in DIR:
        nr, nc = r + dr, c + dc
        if not (0 <= nr < R and 0 <= nc < C):
            print(dist[r][c] + 1)
            ck = True
            break
        
        if grid[nr][nc] == '#' or dist[nr][nc] != -1:
            continue

        nd = dist[r][c] + 1
        if fire_time[nr][nc] <= nd:
            continue
                
        dist[nr][nc] = nd
        jq.append((nr, nc))

if not ck:
    print("IMPOSSIBLE")
