from collections import deque

N = int(input())
arr = [list(input().strip()) for _ in range(N)]
DIR= [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(x, y, color, visited, daltonism=False):
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for dx, dy in DIR:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if daltonism: 
                    if color in ("R", "G") and arr[nx][ny] in ("R", "G"):
                        visited[nx][ny] = True
                        q.append((nx, ny))
                    elif color == "B" and arr[nx][ny] == "B":
                        visited[nx][ny] = True
                        q.append((nx, ny))
                else:  
                    if arr[nx][ny] == color:
                        visited[nx][ny] = True
                        q.append((nx, ny))

def regions(daltonism =False):
    visited = [[False]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i, j, arr[i][j], visited, daltonism)
                cnt += 1
    return cnt

print(regions(False), regions(True))