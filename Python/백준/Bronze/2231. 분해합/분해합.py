N = int(input().strip())

start = max(1, N - 9 * len(str(N)))
ans = 0

for m in range(start, N):
    s = m + sum(int(d) for d in str(m))
    if s == N:
        ans = m
        break

print(ans)
