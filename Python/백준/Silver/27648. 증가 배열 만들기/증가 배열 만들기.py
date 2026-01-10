import sys
n, m, k = map(int, sys.stdin.readline().split())

if n + m - 1 > k:
    print("NO")
else:
    print("YES")
    for i in range(1, n + 1):
        row = [str(i + j) for j in range(m)]
        print(" ".join(row))