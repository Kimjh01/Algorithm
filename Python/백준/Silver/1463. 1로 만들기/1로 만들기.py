import sys
input = sys.stdin.readline

N = int(input().strip())
dp = [0] * (N + 1)  

for i in range(2, N + 1):
    best = dp[i - 1] + 1
    if i % 2 == 0:
        best = min(best, dp[i // 2] + 1)
    if i % 3 == 0:
        best = min(best, dp[i // 3] + 1)
    dp[i] = best

print(dp[N])