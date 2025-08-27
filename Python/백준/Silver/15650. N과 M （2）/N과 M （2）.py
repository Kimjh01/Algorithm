N, M = map(int, input().split())
arr = []

def dfs(start):
    if len(arr) == M:
        print(*arr)
        return
    for x in range(start, N+1):
        arr.append(x)
        dfs(x+1)
        arr.pop()

dfs(1)
