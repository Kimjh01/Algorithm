import sys
input = sys.stdin.readline
tc = int(input())

for _ in range(tc): 
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [0] * (n + 1)
    cnt = 0
    
    for i in range(1, n + 1):
        if visited[i] != 0:
            continue
        
        now = i
        while True:
            visited[now] = i
            now = arr[now]

            if visited[now] == i:
                while visited[now] != -1:
                    visited[now] = -1
                    cnt += 1
                    now = arr[now]
                break
            elif visited[now] != 0:
                break
        
        now = i
        while visited[now] == i:
            visited[now] = -1
            now = arr[now]

    print(n - cnt)