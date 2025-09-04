N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
result = []

def dfs(x):
    if len(result) == M:
        print(*result)
        return
    for y in range(x, N):
        result.append(arr[y])
        dfs(y)  
        result.pop()
        
dfs(0)