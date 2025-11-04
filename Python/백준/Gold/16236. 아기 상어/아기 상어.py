import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
board = []
shark_r = shark_c = 0
for i in range(N):
    row = list(map(int, input().split()))
    for j, v in enumerate(row):
        if v == 9:
            shark_r, shark_c = i, j
            row[j] = 0  
    board.append(row)

DR = (-1, 0, 0, 1)
DC = (0, -1, 1, 0)

def bfs(sr, sc, size):
    dist = [[-1]*N for _ in range(N)]
    q = deque([(sr, sc)])
    dist[sr][sc] = 0

    min_d = float('inf')
    candidates = []  # (r, c)

    while q:
        r, c = q.popleft()
        d = dist[r][c]
        if d > min_d:  
            continue
        for k in range(4):
            nr, nc = r + DR[k], c + DC[k]
            if not (0 <= nr < N and 0 <= nc < N): 
                continue
            if dist[nr][nc] != -1: 
                continue
            if board[nr][nc] > size:  
                continue
            dist[nr][nc] = d + 1
            cell = board[nr][nc]
            if 0 < cell < size:    
                if dist[nr][nc] < min_d:
                    min_d = dist[nr][nc]
                    candidates = [(nr, nc)]
                elif dist[nr][nc] == min_d:
                    candidates.append((nr, nc))
            elif cell == 0 or cell == size:  
                q.append((nr, nc))

    if not candidates:
        return None, None, None

    candidates.sort()
    tr, tc = candidates[0]
    return tr, tc, min_d

size, eaten, time_sum = 2, 0, 0

while True:
    tr, tc, d = bfs(shark_r, shark_c, size)
    if tr is None: 
        break
    time_sum += d
    eaten += 1
    if eaten == size:
        size += 1
        eaten = 0
    board[tr][tc] = 0
    shark_r, shark_c = tr, tc

print(time_sum)