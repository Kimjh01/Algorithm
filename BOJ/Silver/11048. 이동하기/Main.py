import sys
sys.setrecursionlimit(10**6) 
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * M for _ in range(N)]

def dfs(r, c):
    if r < 0 or c < 0:
        return 0
    
    if dp[r][c] != -1:
        return dp[r][c]
    
    dp[r][c] = arr[r][c] + max(dfs(r-1, c), dfs(r, c-1))
    return dp[r][c]

print(dfs(N-1, M-1))