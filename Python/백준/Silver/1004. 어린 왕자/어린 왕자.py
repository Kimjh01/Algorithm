t = int(input())
for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    ans = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        r2 = r * r
        d1 = (x1 - cx) * (x1 - cx) + (y1 - cy) * (y1 - cy)
        d2 = (x2 - cx) * (x2 - cx) + (y2 - cy) * (y2 - cy)
        if (d1 < r2) != (d2 < r2):
            ans += 1
    print(ans)