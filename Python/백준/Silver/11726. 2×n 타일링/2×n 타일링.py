import sys
input = sys.stdin.readline

n = int(input().strip())
MOD = 10007

if n == 1:
    print(1)
    exit()
elif n == 2:
    print(2)
    exit()

dp = [0] * (n + 1)
dp[1], dp[2] = 1, 2

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % MOD

print(dp[n] % MOD)
