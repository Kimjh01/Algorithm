import sys

N, M, a, K = map(int, sys.stdin.readline().split())
other = a - K

t_max = min(N - 1, other)

if other == 0:
    t_min = 0
else:
    t_min = (other + M - 1) // M

print(t_max + 1, t_min + 1)
