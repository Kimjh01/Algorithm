import sys
input = sys.stdin.readline

p, n = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
cnt = 0

for x in a:
    if p < 200:
        p += x
        cnt += 1
    else:
        break
print(cnt)