import sys

input = sys.stdin.readline
n = int(input().strip())
a = list(map(int, input().split()))
arr = [(a[i], i) for i in range(n)]
arr.sort()

p = [0] * n
for rank, (_, idx) in enumerate(arr):
    p[idx] = rank

sys.stdout.write(" ".join(map(str, p)))
