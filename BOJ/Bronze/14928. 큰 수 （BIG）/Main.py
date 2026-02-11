s = input().strip()
m = 20000303
r = 0
for ch in s:
    r = (r * 10 + (ord(ch) - 48)) % m
print(r)
