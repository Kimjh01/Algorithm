N, M = map(int, input().split())
arr = []

def dfs():
    if len(arr) == M:
        print(*arr)
        return
    for x in range(1, N+1):
        arr.append(x)
        dfs()  
        arr.pop()

dfs()