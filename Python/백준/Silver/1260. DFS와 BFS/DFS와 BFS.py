from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()

def dfs(v, visited):
    visited[v] = True
    print(v, end=" ")
    for nxt in graph[v]:
        if not visited[nxt]:
            dfs(nxt, visited)


def bfs(start):
    visited = [False] * (N+1)
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()
        print(v, end=" ")
        for nxt in graph[v]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)

visited = [False] * (N+1)
dfs(V, visited)
print()
bfs(V)