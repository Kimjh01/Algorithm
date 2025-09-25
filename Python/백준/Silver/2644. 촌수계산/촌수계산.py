import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
a, b = map(int, input().split())
m = int(input().strip())

g = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)

dist = [-1] * (n + 1)
q = deque([a])
dist[a] = 0

while q:
    cur = q.popleft()
    if cur == b:
        break
    for nxt in g[cur]:
        if dist[nxt] == -1:
            dist[nxt] = dist[cur] + 1
            q.append(nxt)

print(dist[b])