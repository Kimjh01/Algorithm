import sys
from collections import deque

input = sys.stdin.readline
F, S, G, U, D = map(int, input().split())
visited = [False] * (F + 1)
q = deque([(S, 0)])
visited[S] = True
ck = False

while q:
    cur, dist = q.popleft()
    if cur == G:
        print(dist)
        ck = True
        break
    
    nxt = cur + U
    if U and nxt <= F and not visited[nxt]:
        visited[nxt] = True
        q.append((nxt, dist + 1))
        
    nxt = cur - D
    if D and nxt >= 1 and not visited[nxt]:
        visited[nxt] = True
        q.append((nxt, dist + 1))

if not ck:
    print("use the stairs")