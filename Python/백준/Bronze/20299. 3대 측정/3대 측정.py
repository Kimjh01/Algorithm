import sys
input = sys.stdin.readline

N, K, L = map(int, input().split())
cnt = 0
chosen = []

for _ in range(N):
    team = list(map(int, input().split()))
    if min(team) >= L and sum(team) >= K:
        cnt += 1
        chosen.extend(team)

print(cnt)
if chosen:
    print(*chosen)
else:
    print()