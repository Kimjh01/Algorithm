import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

parent = [0] * (n + 1)
q = deque([1])
parent[1] = -1  

while q:
    v = q.popleft()
    for w in g[v]:
        if parent[w] == 0:     
            parent[w] = v
            q.append(w)

print("\n".join(str(parent[i]) for i in range(2, n + 1)))