d = list(map(int, open(0).read().split()))
n = d[0]
a = []
idx = 1
for _ in range(n):
    a.append(d[idx:idx+n])
    idx += n

h = [[0]*n for _ in range(n)]
v = [[0]*n for _ in range(n)]
g = [[0]*n for _ in range(n)]

h[0][1] = 1

for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            continue
        if j + 1 < n and a[i][j+1] == 0:
            h[i][j+1] += h[i][j] + g[i][j]
            
        if i + 1 < n and a[i+1][j] == 0:
            v[i+1][j] += v[i][j] + g[i][j]
            
        if i + 1 < n and j + 1 < n:
            if a[i][j+1] == 0 and a[i+1][j] == 0 and a[i+1][j+1] == 0:
                g[i+1][j+1] += h[i][j] + v[i][j] + g[i][j]

print(h[n-1][n-1] + v[n-1][n-1] + g[n-1][n-1])
