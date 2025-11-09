import sys
sys.setrecursionlimit(10**7)

n = int(sys.stdin.readline())

def prod(l, r):
    if l > r:
        return 1
    if l == r:
        return l
    m = (l + r) // 2
    return prod(l, m) * prod(m + 1, r)

if n == 0:
    print(1)
else:
    print(prod(1, n))
