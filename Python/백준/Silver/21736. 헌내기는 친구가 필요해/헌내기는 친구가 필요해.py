import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
campus = [list(input().strip()) for _ in range(N)]

sy = sx = -1
for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            sy, sx = i, j
            break
    if sy != -1:
        break

visited = [[False]*M for _ in range(N)]
q = deque([(sy, sx)])
visited[sy][sx] = True

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)

cnt = 0
while q:
    y, x = q.popleft()
    if campus[y][x] == 'P':
        cnt += 1
    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]
        if 0 <= ny < N and 0 <= nx < M:
            if not visited[ny][nx] and campus[ny][nx] != 'X':
                visited[ny][nx] = True
                q.append((ny, nx))

print(cnt if cnt > 0 else "TT")
