from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]   
dist = [[-1] * M for _ in range(N)]

x, y = 0, 0

q = deque([(x, y)])
dist[x][y] = 1

while q:
    x, y = q.popleft()
    if x == N-1 and y == M-1:
        break

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1 and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))

print(dist[N-1][M-1])
