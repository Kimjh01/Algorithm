def turret(x1, y1, r1, x2, y2, r2):
    dx = x1 - x2
    dy = y1 - y2
    d2 = dx * dx + dy * dy  
    S = (r1 + r2) * (r1 + r2) 
    D = (r1 - r2) * (r1 - r2)
    if d2 == 0 and r1 == r2:
        return -1

    if d2 == S or d2 == D:
        return 1

    if D < d2 < S:
        return 2

    return 0

N = int(input())
for _ in range(N):
    arr = list(map(int, input().split()))
    print(turret(*arr))