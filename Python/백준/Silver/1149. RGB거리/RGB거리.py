import sys
input = sys.stdin.readline

N = int(input().strip())
r, g, b = map(int, input().split())
dpR, dpG, dpB = r, g, b

for _ in range(2, N+1):
    r, g, b = map(int, input().split())
    nR = r + min(dpG, dpB)
    nG = g + min(dpR, dpB)
    nB = b + min(dpR, dpG)
    dpR, dpG, dpB = nR, nG, nB

print(min(dpR, dpG, dpB))
