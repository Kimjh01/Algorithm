from collections import deque
import sys
MAX = 100000
N, K = map(int, input().split())

if N >= K:
    print(N - K)
    sys.exit(0)

dist = [-1] * (MAX + 1)
q = deque([N])
dist[N] = 0

while q:
    x = q.popleft()
    if x == K:
        print(dist[x])
        break
    for nx in (x - 1, x + 1, x * 2):
        if 0 <= nx <= MAX and dist[nx] == -1:
            dist[nx] = dist[x] + 1
            q.append(nx)
