import sys

T = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(T)]
N = max(nums)

dp = [0] * (max(3, N) + 1)
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, N + 1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

print("\n".join(str(dp[n]) for n in nums))
