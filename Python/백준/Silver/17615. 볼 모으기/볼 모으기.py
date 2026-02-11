import sys

input = sys.stdin.readline
n = int(input().strip())
s = input().strip()

r = s.count('R')
b = n - r

leftR = 0
for ch in s:
    if ch == 'R':
        leftR += 1
    else:
        break

rightR = 0
for ch in reversed(s):
    if ch == 'R':
        rightR += 1
    else:
        break

leftB = 0
for ch in s:
    if ch == 'B':
        leftB += 1
    else:
        break

rightB = 0
for ch in reversed(s):
    if ch == 'B':
        rightB += 1
    else:
        break

ans = min(r - leftR, r - rightR, b - leftB, b - rightB)
print(ans)
