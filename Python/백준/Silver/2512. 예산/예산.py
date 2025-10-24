import sys

input = sys.stdin.readline
n = int(input())
requests = list(map(int, input().split()))
total = int(input())

if sum(requests) <= total:
    print(max(requests))
    sys.exit(0)

lo, hi = 0, max(requests)
ans = 0
while lo <= hi:
    mid = (lo + hi) // 2  
    s = 0
    for r in requests:
        s += r if r <= mid else mid
    if s <= total:
        ans = mid     
        lo = mid + 1
    else:
        hi = mid - 1

print(ans)