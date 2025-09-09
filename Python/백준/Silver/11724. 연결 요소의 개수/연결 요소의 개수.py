import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
cnt= 0

def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        for nxt in graph[v]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)

for i in range(1, N + 1):
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)