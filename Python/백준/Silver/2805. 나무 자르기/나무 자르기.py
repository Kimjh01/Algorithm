N, M = map(int, input().split())
arr = list(map(int, input().split()))

lo, hi = 0, max(arr)
ans = 0

while lo <= hi:
    mid = (lo + hi) // 2

    total = 0
    for tree in arr:
        if tree > mid:
            total += tree - mid
            if total >= M:
                break

    if total >= M:
        ans = mid        
        lo = mid + 1
    else:
        hi = mid - 1

print(ans)