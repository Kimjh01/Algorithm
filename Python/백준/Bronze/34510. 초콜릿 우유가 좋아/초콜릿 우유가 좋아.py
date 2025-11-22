import sys

a, b, c, n = map(int, sys.stdin.read().split())
print((a + b) * (n & 1) + b * (n // 2) + c * n)
