import sys
input = sys.stdin.readline

N = int(input().strip())
r, g, b = map(int, input().split())

for _ in range(2, N+1):
    R, G, B = map(int, input().split())
    nR = R + min(g, b)
    nG = G + min(r, b)
    nB = B + min(r, g)
    r, g, b = nR, nG, nB

print(min(r, g, b))