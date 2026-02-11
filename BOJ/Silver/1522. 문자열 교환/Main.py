import sys
inout = sys.stdin.readline
s = input().strip()
n = len(s)
k = s.count('a')

if k == 0 or k == n:
    print(0)
    sys.exit(0)

t = s + s

b = 0
for i in range(k):
    if t[i] == 'b':
        b += 1

ans = b
for i in range(1, n):
    if t[i - 1] == 'b':
        b -= 1
    if t[i + k - 1] == 'b':
        b += 1
    if b < ans:
        ans = b

print(ans)
