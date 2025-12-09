import sys
input = sys.stdin.readline

n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def dfs(i):
    global ans
    if i == n:
        cnt = 0
        for j in range(n):
            if eggs[j][0] <= 0:
                cnt += 1
        ans = max(ans, cnt)
        return

    if eggs[i][0] <= 0:
        dfs(i + 1)
        return

    check = False
    for j in range(n):
        if i == j or eggs[j][0] <= 0:
            continue
        
        check = True
        eggs[i][0] -= eggs[j][1]
        eggs[j][0] -= eggs[i][1]
        
        dfs(i + 1)
        
        eggs[i][0] += eggs[j][1]
        eggs[j][0] += eggs[i][1]
        
    if not check:
        dfs(i + 1)

dfs(0)
print(ans)