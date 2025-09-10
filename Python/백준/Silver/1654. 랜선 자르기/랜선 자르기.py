K, N = map(int,input().split())
arr = [ int(input()) for _ in range(K)]
ans = 0
low, high = 1, max(arr)
while low <= high:
    mid = (low + high) // 2
    temp = sum( x // mid for x in arr)
    if temp >= N:
        ans = mid
        low = mid + 1
    else:
        high = mid - 1

print(ans)