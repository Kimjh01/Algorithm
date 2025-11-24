import sys
input = sys.stdin.readline

N, C = map(int, input().split())
periods = set()
has_one = False

for _ in range(N):
    p = int(input())
    if p == 1:
        print(C)
        sys.exit(0)
    periods.add(p)

fire = [0] * (C + 1)

for p in periods:
    for t in range(p, C + 1, p):
        fire[t] = 1

print(sum(fire))
