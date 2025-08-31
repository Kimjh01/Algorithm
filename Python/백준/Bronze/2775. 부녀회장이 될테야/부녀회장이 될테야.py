import sys, math
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    print(math.comb(n + k, k + 1))