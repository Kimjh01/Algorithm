import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]

print(M)
for x in range(M):
    row = []
    for j in range(N):
        row.append(A[(x + j) % M][j])
    print(*row)
