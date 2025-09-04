N, M = map(int, input().split())
arr = []

def dfs(x):
    if len(arr) == M:
        print(*arr)
        return
    for y in range(x, N+1):
        arr.append(y)
        dfs(y)  
        arr.pop()

dfs(1)