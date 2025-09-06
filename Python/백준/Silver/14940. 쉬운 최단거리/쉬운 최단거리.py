from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]   
dist = [[-1] * M for _ in range(N)]

x = y = -1
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            x, y = i, j
            break
    if x != -1:
        break

q = deque([(x, y)])
dist[x][y] = 0

while q:
    x, y = q.popleft()
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and dist[nx][ny] == -1 and arr[nx][ny] == 1:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))

for i in range(N):
    row = []
    for j in range(M):
        if arr[i][j] == 0:
            row.append(0)
        else:
            row.append(dist[i][j])
    print(*row)
