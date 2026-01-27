import sys

input = sys.stdin.readline

n = int(input().strip())
a = list(map(int, input().split()))
op = list(map(int, input().split()))

mx = -10**18
mn = 10**18

stack = [(1, a[0], op[0], op[1], op[2], op[3])]

while stack:
    i, cur, p, m, t, d = stack.pop()
    if i == n:
        if cur > mx:
            mx = cur
        if cur < mn:
            mn = cur
        continue

    x = a[i]

    if p:
        stack.append((i + 1, cur + x, p - 1, m, t, d))
    if m:
        stack.append((i + 1, cur - x, p, m - 1, t, d))
    if t:
        stack.append((i + 1, cur * x, p, m, t - 1, d))
    if d:
        if cur < 0:
            nx = -(abs(cur) // x)
        else:
            nx = cur // x
        stack.append((i + 1, nx, p, m, t, d - 1))

print(mx)
print(mn)
