T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    res = -1
    ck = True
    for i in range(N):
        for j in range(i+1, N):
            ck = True
            val = arr[i]*arr[j]
            temp = str(val)
            for k in range(len(temp)-1):
                if temp[k] > temp[k+1]:
                    ck = False
                    break
            if ck and res < val:
                res = val
                

    print(f"#{tc} {res}")