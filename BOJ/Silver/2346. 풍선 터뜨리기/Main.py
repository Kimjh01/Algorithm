import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
moves = list(map(int, input().split()))

dq = deque((i + 1, moves[i]) for i in range(n))
ans = []

while dq:
    idx, k = dq.popleft()
    ans.append(idx)
    if not dq:
        break
    if k > 0:
        dq.rotate(-(k - 1))  
    else:
        dq.rotate(-k)    

print(*ans)
