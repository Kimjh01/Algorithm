import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

g = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[b].append(a)

visited = [0] * (n + 1)
visit = 0

best = 0
ans = []

for start in range(1, n + 1):
    visit += 1
    q = deque([start])
    visited[start] = visit
    cnt = 1

    while q:
        x = q.popleft()
        for nx in g[x]:
            if visited[nx] != visit:
                visited[nx] = visit
                q.append(nx)
                cnt += 1

    if cnt > best:
        best = cnt
        ans = [start]
    elif cnt == best:
        ans.append(start)

print(*ans)
