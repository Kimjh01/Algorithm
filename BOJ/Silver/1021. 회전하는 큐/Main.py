import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
tar = list(map(int, input().split()))

d = deque(range(1, n + 1))
ans = 0

for x in tar:
    idx = d.index(x)
    if idx <= len(d) // 2:
        d.rotate(-idx)
        ans += idx
    else:
        r = len(d) - idx
        d.rotate(r)
        ans += r
    d.popleft()

print(ans)
