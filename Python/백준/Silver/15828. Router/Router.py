import sys
from collections import deque
input = sys.stdin.readline

N = int(input())    
q = deque()

while True:
    x = int(input())
    if x == -1:   
        break
    elif x == 0:
        if q:
            q.popleft()
    else:       
        if len(q) < N:
            q.append(x)
if not q:
    print("empty")
else:
    print(" ".join(map(str, q)))
