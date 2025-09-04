N, M = map(int, input().split())
arr = sorted(set(map(int, input().split())))
result = []

def dfs(x):
    if len(result) == M:
        print(*result)
        return
    for y in range(x, len(arr)):
        result.append(arr[y])
        dfs(y)  
        result.pop()
        
dfs(0)
