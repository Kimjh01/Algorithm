import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])

idx = 2
min_pkg = 1001
min_single = 1001

for _ in range(M):
    p = int(data[idx])
    s = int(data[idx+1])
    idx += 2
    if p < min_pkg: min_pkg = p
    if s < min_single: min_single = s
    
cost1 = ((N // 6) + 1) * min_pkg
cost2 = (N // 6) * min_pkg + (N % 6) * min_single
cost3 = N * min_single

print(min(cost1, cost2, cost3))