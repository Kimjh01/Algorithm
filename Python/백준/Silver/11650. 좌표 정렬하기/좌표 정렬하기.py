N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
result = []
arr = sorted(arr)
for row in arr:
    print(*row)
    
