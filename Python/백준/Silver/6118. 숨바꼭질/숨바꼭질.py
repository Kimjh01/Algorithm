n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

dist = [-1] * (n + 1)
dist[1] = 0
queue = [1]

head = 0
while head < len(queue):
    curr = queue[head]
    head += 1
    for neighbor in adj[curr]:
        if dist[neighbor] == -1:
            dist[neighbor] = dist[curr] + 1
            queue.append(neighbor)

max_dist = max(dist)
first_node = dist.index(max_dist)
count = dist.count(max_dist)

print(first_node, max_dist, count)