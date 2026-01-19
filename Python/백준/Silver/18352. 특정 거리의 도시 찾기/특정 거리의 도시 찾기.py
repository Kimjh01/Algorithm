import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

dist = [-1] * (n + 1)
dist[x] = 0
q = deque([x])

while q:
    now = q.popleft()
    for nxt in graph[now]:
        if dist[nxt] == -1:
            dist[nxt] = dist[now] + 1
            q.append(nxt)

ans = []
for i in range(1, n + 1):
    if dist[i] == k:
        ans.append(i)

if not ans:
    print(-1)
else:
    for i in ans:
        print(i)