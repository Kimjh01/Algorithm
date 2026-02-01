n = int(input())
cnt = [0] * n

stack = [(0, n - 1, 0)]
while stack:
    s, e, add = stack.pop()
    if s > e:
        continue
    mid = (s + e) // 2
    cnt[mid] += add
    add += 1
    stack.append((s, mid - 1, add))
    stack.append((mid + 1, e, add))

stack = [(0, n - 1, 0)]
while stack:
    s, e, sub = stack.pop()
    if s > e:
        continue
    if s == e:
        cnt[s] -= sub
        continue
    t1 = s + (e - s) // 3
    t2 = e - (e - s) // 3
    cnt[t1] -= sub
    sub += 1
    cnt[t2] -= sub
    sub += 1
    stack.append((s, t1 - 1, sub))
    stack.append((t1 + 1, t2 - 1, sub))
    stack.append((t2 + 1, e, sub))

res1 = res2 = res3 = 0
for x in cnt:
    if x < 0:
        res1 += 1
    elif x == 0:
        res2 += 1
    else:
        res3 += 1

print(f"{res1}\n{res2}\n{res3}")