import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

homes, shops = [], []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            homes.append((i, j))
        elif city[i][j] == 2:
            shops.append((i, j))

H, C = len(homes), len(shops)

dist = [[0]*C for _ in range(H)]
for hi, (hx, hy) in enumerate(homes):
    for sj, (sx, sy) in enumerate(shops):
        dist[hi][sj] = abs(hx - sx) + abs(hy - sy)

INF = float('inf')

if M == C:
    total = 0
    for hi in range(H):
        total += min(dist[hi][sj] for sj in range(C))
    print(total)
    sys.exit(0)

best = INF

for comb in combinations(range(C), M):
    total = 0
    for hi in range(H):
        total += min(dist[hi][sj] for sj in comb)
        if total >= best:      
            break
    else:
        if total < best:
            best = total

print(best)