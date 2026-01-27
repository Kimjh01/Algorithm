import sys

input = sys.stdin.readline
n = int(input().strip())
a = list(map(int, input().split()))

ans = 0
for i in range(n - 3):
    for j in range(i + 1, n - 2):
        for k in range(j + 1, n - 1):
            p1 = 1
            for t in range(0, i + 1):
                p1 *= a[t]
            p2 = 1
            for t in range(i + 1, j + 1):
                p2 *= a[t]
            p3 = 1
            for t in range(j + 1, k + 1):
                p3 *= a[t]
            p4 = 1
            for t in range(k + 1, n):
                p4 *= a[t]
            s = p1 + p2 + p3 + p4
            if s > ans:
                ans = s
print(ans)
