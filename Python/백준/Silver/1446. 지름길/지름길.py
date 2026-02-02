import sys
input = sys.stdin.readline

n, d = map(int, input().split())
way = []
for _ in range(n):
    way.append(list(map(int, input().split())))

dist = [i for i in range(d + 1)]

for i in range(d + 1):
    if i > 0:
        dist[i] = min(dist[i], dist[i-1] + 1)
    
    for s, e, w in way:
        if i == s and e <= d and dist[i] + w < dist[e]:
            dist[e] = dist[i] + w

print(dist[d])