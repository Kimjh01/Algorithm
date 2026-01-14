import sys

input = sys.stdin.read
data = list(map(int, input().split()))

n1 = data[0] * 1000 + data[1] * 100 + data[2] * 10 + data[3]
n2 = data[1] * 1000 + data[2] * 100 + data[3] * 10 + data[0]
n3 = data[2] * 1000 + data[3] * 100 + data[0] * 10 + data[1]
n4 = data[3] * 1000 + data[0] * 100 + data[1] * 10 + data[2]

target = min(n1, n2, n3, n4)
cnt = 0

for i in range(1111, target + 1):
    s = str(i)
    if '0' in s:
        continue
    
    a, b, c, d = int(s[0]), int(s[1]), int(s[2]), int(s[3])
    c1 = a * 1000 + b * 100 + c * 10 + d
    c2 = b * 1000 + c * 100 + d * 10 + a
    c3 = c * 1000 + d * 100 + a * 10 + b
    c4 = d * 1000 + a * 100 + b * 10 + c
    
    clock_num = min(c1, c2, c3, c4)
    
    if clock_num == i:
        cnt += 1

print(cnt)