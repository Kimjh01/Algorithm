x, y, p1, p2 = map(int, input().split())

ans = -1
while p1 <= 1000000 and p2 <= 1000000:
    if p1 == p2:
        ans = p1
        break
    if p1 < p2:
        p1 += x
    else:
        p2 += y

print(ans)