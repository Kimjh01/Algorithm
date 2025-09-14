import sys, heapq
input = sys.stdin.readline

N = int(input())
h = []
out = []
for _ in range(N):
    x = int(input())
    if x == 0:
        out.append(str(heapq.heappop(h)) if h else '0')
    else:
        heapq.heappush(h, x)
print('\n'.join(out))