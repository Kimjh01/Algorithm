import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
reach = [[0]*N for _ in range(N)]

for s in range(N):
    q = deque()
    visited = [0]*N
    for v in range(N):
        if G[s][v]:
            q.append(v)
            visited[v] = 1
            reach[s][v] = 1
    while q:
        u = q.popleft()
        for v in range(N):
            if G[u][v] and not visited[v]:
                visited[v] = 1
                reach[s][v] = 1
                q.append(v)

for i in range(N):
    print(*reach[i])
