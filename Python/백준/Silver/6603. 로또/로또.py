def dfs(depth, start):
    if depth == 6:                        
        print(' '.join(map(str, path)))
        return
    for i in range(start, N):              
        path.append(arr[i])
        dfs(depth + 1, i + 1)             
        path.pop()

while True:
    raw = list(map(int, input().split()))
    if raw[0] == 0:
        break
    arr = raw[1:]                                             
    N = len(arr)
    path = []
    dfs(0, 0)
    print()