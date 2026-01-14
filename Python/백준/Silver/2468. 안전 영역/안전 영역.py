import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

max_h = 0
for row in graph:
    curr_max = max(row)
    if curr_max > max_h:
        max_h = curr_max

ans = 0

for h in range(max_h):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] > h and not visited[i][j]:
                cnt += 1
                q = deque([(i, j)])
                visited[i][j] = True
                
                while q:
                    x, y = q.popleft()
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N:
                            if not visited[nx][ny] and graph[nx][ny] > h:
                                visited[nx][ny] = True
                                q.append((nx, ny))
    if cnt > ans:
        ans = cnt

print(ans)