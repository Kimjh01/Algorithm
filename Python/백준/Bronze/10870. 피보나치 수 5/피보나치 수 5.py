def fibo(n):
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1
    dp = [0] * (n+1)
    dp[1], dp[2] = 1, 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

N = int(input())
print(fibo(N))