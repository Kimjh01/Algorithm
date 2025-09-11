import sys
from collections import deque
input = sys.stdin.readline

DIRS = [(1,0), (-1,0), (0,1), (0,-1)]

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split()) 
    board = [[0]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        board[y][x] = 1

    visited = [[False]*M for _ in range(N)]

    def bfs(sr, sc):
        q = deque([(sr, sc)])
        visited[sr][sc] = True
        while q:
            r, c = q.popleft()
            for dr, dc in DIRS:
                nr, nc = r+dr, c+dc
                if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and board[nr][nc] == 1:
                    visited[nr][nc] = True
                    q.append((nr, nc))

    worms = 0
    for r in range(N):
        for c in range(M):
            if board[r][c] == 1 and not visited[r][c]:
                bfs(r, c)
                worms += 1
    print(worms)