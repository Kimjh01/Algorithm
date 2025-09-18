from collections import deque

N = int(input())
board = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)

def bfs(sy, sx):
    q = deque([(sy, sx)])
    visited[sy][sx] = True
    cnt = 1
    while q:
        y, x = q.popleft()
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if 0 <= ny < N and 0 <= nx < N:
                if not visited[ny][nx] and board[ny][nx] == 1:
                    visited[ny][nx] = True
                    cnt += 1
                    q.append((ny, nx))
    return cnt

sizes = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and not visited[i][j]:
            sizes.append(bfs(i, j))

sizes.sort()
print(len(sizes))
print(*sizes, sep="\n")
