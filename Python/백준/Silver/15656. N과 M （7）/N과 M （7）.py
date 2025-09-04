N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
result = []

def dfs():
    if len(result) == M:
        print(*result)
        return
    for x in range(N):
        result.append(arr[x])
        dfs()  
        result.pop()
        
dfs()
