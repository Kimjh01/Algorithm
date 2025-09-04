N, M = map(int, input().split())
arr = sorted(set(map(int, input().split())))
result = []

def dfs():
    if len(result) == M:
        print(*result)
        return
    for y in range(len(arr)):
        result.append(arr[y])
        dfs()  
        result.pop()
        
dfs()