import sys

input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().split()))

chk = [False] * (n + 2)

limit = n + 1
for x in arr:
    if 1 <= x <= limit:
        chk[x] = True

ans = 1
while ans <= limit and chk[ans]:
    ans += 1

print(ans)
