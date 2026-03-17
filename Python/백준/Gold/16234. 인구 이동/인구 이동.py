from collections import deque
import sys

input = sys.stdin.readline

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    countries = [(x, y)]
    total = graph[x][y]

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(graph[cx][cy] - graph[nx][ny]) <= r:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    countries.append((nx, ny))
                    total += graph[nx][ny]

    return countries, total

days = 0

while True:
    visited = [[False] * n for _ in range(n)]
    moved = False

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                countries, total = bfs(i, j, visited)

                if len(countries) > 1:
                    moved = True
                    new_pop = total // len(countries)
                    for x, y in countries:
                        graph[x][y] = new_pop

    if not moved:
        break

    days += 1

print(days)