import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n, m, w = map(int, input().split())
    edges = []

    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
            
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    dist = [0] * (n + 1)
    negative_cycle = False

    for i in range(1, n + 1):
        updated = False
        for u, v, cost in edges:
            if dist[v] > dist[u] + cost:
                dist[v] = dist[u] + cost
                updated = True
                if i == n:
                    negative_cycle = True
                    break
        if not updated:
            break

    print("YES" if negative_cycle else "NO")