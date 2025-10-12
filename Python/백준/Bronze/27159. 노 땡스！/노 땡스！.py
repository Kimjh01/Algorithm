n = int(input().strip())
arr = list(map(int, input().split()))

ans = 0
prev = None
for x in arr:
    if prev is None or x != prev + 1: 
        ans += x
    prev = x

print(ans)
