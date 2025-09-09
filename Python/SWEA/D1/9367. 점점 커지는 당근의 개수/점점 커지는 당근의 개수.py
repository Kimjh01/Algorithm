T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    res, temp, cnt = 1, 1, 1
    for i in range(1, N):
        if arr[i-1] < arr[i]:cnt+=1;temp = cnt
        else:cnt = 1
        res = max(res, temp)
    print(f'#{tc} {res}')