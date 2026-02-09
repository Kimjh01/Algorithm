d = list(map(int, open(0).read().split()))
a = d[0:5]
b = d[5:10]
wa = d[10:15]
wb = d[15:20]

ca = a[0] * (100 + a[1]) * ((10000 - min(100 * a[2], 10000)) + min(a[2], 100) * a[3]) * (100 + a[4])
cb = b[0] * (100 + b[1]) * ((10000 - min(100 * b[2], 10000)) + min(b[2], 100) * b[3]) * (100 + b[4])

a2 = [a[0]-wa[0]+wb[0], a[1]-wa[1]+wb[1], a[2]-wa[2]+wb[2], a[3]-wa[3]+wb[3], a[4]-wa[4]+wb[4]]
b2 = [b[0]-wb[0]+wa[0], b[1]-wb[1]+wa[1], b[2]-wb[2]+wa[2], b[3]-wb[3]+wa[3], b[4]-wb[4]+wa[4]]

ca2 = a2[0] * (100 + a2[1]) * ((10000 - min(100 * a2[2], 10000)) + min(a2[2], 100) * a2[3]) * (100 + a2[4])
cb2 = b2[0] * (100 + b2[1]) * ((10000 - min(100 * b2[2], 10000)) + min(b2[2], 100) * b2[3]) * (100 + b2[4])

out = []
out.append("+" if ca2 > ca else ("-" if ca2 < ca else "0"))
out.append("+" if cb2 > cb else ("-" if cb2 < cb else "0"))
print("\n".join(out))
