import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(range(101))  
for _ in range(N + M):
    a, b = map(int, input().split())
    arr[a] = b          

start = 1
while arr[start] != start:  
    start = arr[start]

visited = [False] * 101
visited[start] = True

q = deque([(start, 0)])  

while q:
    pos, throws = q.popleft()
    if pos == 100:
        print(throws)
        break
    for d in range(1, 7):
        nxt = pos + d
        if nxt > 100:
            continue
  
        while arr[nxt] != nxt:
            nxt = arr[nxt]
        if not visited[nxt]:
            visited[nxt] = True
            if nxt == 100:
                print(throws + 1)
                q.clear()
                break
            q.append((nxt, throws + 1))
