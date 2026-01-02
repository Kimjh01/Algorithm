import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

current_sum = 0
ans = -1

for i in range(N - 1, -1, -1):
    current_sum += A[i]
    if current_sum >= M:
        ans = i + 1
        break

print(ans)