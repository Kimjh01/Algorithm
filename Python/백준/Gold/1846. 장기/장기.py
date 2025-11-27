import sys

n = int(sys.stdin.readline())

if n == 3:
    print(-1)
    sys.exit()

ans = [(i + n // 2) % n + 1 for i in range(n)]

for i in range(n):
    if (i + 1) + ans[i] == n + 1:
        if i < n - 1:
            ans[i], ans[i+1] = ans[i+1], ans[i]
        else:
            ans[i], ans[i-1] = ans[i-1], ans[i]
for x in ans:
    print(x)