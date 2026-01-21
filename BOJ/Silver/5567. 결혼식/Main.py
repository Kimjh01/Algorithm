import sys
from collections import deque

input = sys.stdin.readline
n = int(input().strip()) # 전체 동기의 수
m = int(input().strip()) # 동기끼리 친구관계 

g = [[] for _ in range(n + 1)] # 방향향 그래프 초기화

# 친구끼리 정보 저장
for _ in range(m):
    a, b = map(int, input().split()) 
    g[a].append(b)
    g[b].append(a)

# 동기끼리 관계여부를 위한 
dist = [-1] * (n + 1)
q = deque([1])
dist[1] = 0

# 방문 여부와 거리 확인해서 가지처버리기 
while q:
    x = q.popleft()
    if dist[x] == 2:
        continue
    for y in g[x]:
        if dist[y] == -1:
            dist[y] = dist[x] + 1
            q.append(y)

# 범위 내에 친구관계 수 합산
ans = 0
for i in range(2, n + 1):
    if 1 <= dist[i] <= 2:
        ans += 1
print(ans)
