import sys
import heapq
input = sys.stdin.readline

INF = 10**18

V, E = map(int, input().split())
K = int(input())
adj = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))  

dist = [INF] * (V + 1)
dist[K] = 0
pq = [(0, K)]  

while pq:
    d, u = heapq.heappop(pq)
    if d != dist[u]:  
        continue
    for v, w in adj[u]:
        nd = d + w
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))

out = []
for i in range(1, V + 1):
    if dist[i] == INF:
        out.append("INF")
    else:
        out.append(str(dist[i]))
print("\n".join(out))
