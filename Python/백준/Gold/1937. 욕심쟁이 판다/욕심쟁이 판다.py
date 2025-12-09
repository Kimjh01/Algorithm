import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if dp[x][y]:
        return dp[x][y]
    
    dp[x][y] = 1
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < n:
            if a[nx][ny] > a[x][y]:
                dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
                
    return dp[x][y]

ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j))

print(ans)