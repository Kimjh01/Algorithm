N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

cnt = 0
while M > 0:
    t = arr.pop()
    coin = M // t 
    if coin > 0:
        cnt += coin
        M -= coin * t

print(cnt)