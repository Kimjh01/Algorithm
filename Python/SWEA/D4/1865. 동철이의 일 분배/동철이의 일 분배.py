T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j] /= 100

    res = 0.0

    def dfs(hu, visited, p):
        global res
        if p <= res:
            return
        if hu == N:
            res = p
            return
        for j in range(N):
            if not visited[j]:
                visited[j] = True
                dfs(hu+1, visited, p * arr[hu][j])
                visited[j] = False

    visited = [False]*N
    dfs(0, visited, 1.0)
    print(f"#{tc} {res*100:.6f}")