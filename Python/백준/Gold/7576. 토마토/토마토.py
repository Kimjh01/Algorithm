import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dist = [[-1] * M for _ in range(N)]
q = deque()

for r in range(N):
    for c in range(M):
        if board[r][c] == 1:
            dist[r][c] = 0
            q.append((r, c))

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while q:
    r, c = q.popleft()
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M:
            if board[nr][nc] == 0 and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))

ans = 0
for r in range(N):
    for c in range(M):
        if board[r][c] == -1:
            continue
        if board[r][c] == 0 and dist[r][c] == -1:
            print(-1)
            sys.exit(0)
        if dist[r][c] != -1:
            ans = max(ans, dist[r][c])

print(ans)
