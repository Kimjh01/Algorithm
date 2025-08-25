import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
cost = [0] + list(map(int, input().split()))

g = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

visited = [False] * (N + 1)

def dfs_start(s):
    stack = [s]
    visited[s] = True
    mn = cost[s]
    while stack:
        u = stack.pop()
        if cost[u] < mn:
            mn = cost[u]
        for v in g[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)
    return mn

total = 0
for v in range(1, N + 1):
    if not visited[v]:
        total += dfs_start(v)

print(total if total <= K else "Oh no")
