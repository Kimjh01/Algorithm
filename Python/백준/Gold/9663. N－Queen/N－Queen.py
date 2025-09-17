import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
col = [False]*N
diag1 = [False]*(2*N)   
diag2 = [False]*(2*N)   
cnt = 0

def dfs(r: int):
    global cnt
    if r == N:
        cnt += 1
        return
    for c in range(N):
        d1 = r + c
        d2 = r - c + (N - 1)
        if not col[c] and not diag1[d1] and not diag2[d2]:
            col[c] = diag1[d1] = diag2[d2] = True
            dfs(r + 1)
            col[c] = diag1[d1] = diag2[d2] = False

dfs(0)
print(cnt)