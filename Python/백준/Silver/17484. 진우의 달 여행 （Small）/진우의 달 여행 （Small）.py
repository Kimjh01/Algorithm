n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

INF = 10**15
dp = [[[INF] * 3 for _ in range(m)] for _ in range(n)]

for c in range(m):
    for d in range(3):
        dp[0][c][d] = grid[0][c]

for r in range(1, n):
    for c in range(m):
        v = grid[r][c]
        if c > 0:
            dp[r][c][0] = min(dp[r-1][c-1][1], dp[r-1][c-1][2]) + v
        
        dp[r][c][1] = min(dp[r-1][c][0], dp[r-1][c][2]) + v
        
        if c < m - 1:
            dp[r][c][2] = min(dp[r-1][c+1][0], dp[r-1][c+1][1]) + v

ans = INF
for c in range(m):
    for d in range(3):
        if dp[n-1][c][d] < ans:
            ans = dp[n-1][c][d]

print(ans)