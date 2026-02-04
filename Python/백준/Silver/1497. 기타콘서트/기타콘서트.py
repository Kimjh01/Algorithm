n, m = map(int, input().split())
v = []
for _ in range(n):
    _, s = input().split()
    b = 0
    for i in range(m):
        if s[i] == 'Y':
            b |= (1 << i)
    v.append(b)

x = 0
y = -1

for i in range(1, 1 << n):
    c = 0
    k = 0
    for j in range(n):
        if (i >> j) & 1:
            c |= v[j]
            k += 1
    
    cnt = bin(c).count('1')
    
    if cnt > x:
        x = cnt
        y = k
    elif cnt == x and cnt > 0:
        if y == -1 or k < y:
            y = k

if x == 0:
    print(-1)
else:
    print(y)