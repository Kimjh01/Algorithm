m, n = map(int, input().split())

if m <= n:
    print(2 * (m - 1))
else:
    print(2 * (n - 1) + 1)