import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
g = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

def bfs(start: int) -> int:
    dist = [-1] * (N + 1)
    q = deque([start])
    dist[start] = 0
    total = 0

    while q:
        cur = q.popleft()
        for nxt in g[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                total += dist[nxt]
                q.append(nxt)
    return total

best_person = 1
best_score = bfs(1)

for i in range(2, N + 1):
    score = bfs(i)
    if score < best_score:
        best_score = score
        best_person = i

print(best_person)
