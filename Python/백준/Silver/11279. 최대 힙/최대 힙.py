import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())
hq = [] 
for _ in range(N):
    x = int(input())
    if x:                    
        heappush(hq, -x) 
    else:
        if hq:
            print(-heappop(hq))
        else:
            print(0)
