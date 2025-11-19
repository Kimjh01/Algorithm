import sys

input = sys.stdin.readline

N = int(input())
scores = list(map(int, input().split()))

dp = [0] * (N + 1) 

for i in range(1, N + 1):
    max_v = 0
    min_v = 10001
    for j in range(i, 0, -1):
        max_v = max(max_v, scores[j - 1])
        min_v = min(min_v, scores[j - 1])
        dp[i] = max(dp[i], dp[j - 1] + (max_v - min_v))

print(dp[N])
