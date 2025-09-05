s = input().strip()

r = s.index('@')
b = s.index('#')
g = s.index('!')

if (r < b < g) or (g < b < r):
    print(abs(g - r) - 1)
else:
    print(-1)
