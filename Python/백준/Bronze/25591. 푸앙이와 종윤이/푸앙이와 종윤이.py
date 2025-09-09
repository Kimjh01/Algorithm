A, B = map(int, input().split())
res = []
a = 100-A
res.append(a)
b = 100-B
res.append(b)
c = 100-(a+b)
res.append(c)
d = a*b
res.append(d)
q = d // 100
res.append(q)
r = d % 100
res.append(r)
print(' '.join(map(str, res)))
print(c+q, r)