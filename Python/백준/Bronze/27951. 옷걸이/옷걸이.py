import sys

input = sys.stdin.readline
n = int(input().strip())
types = list(map(int, input().split()))
u, d = map(int, input().split())

c1 = types.count(1)
c2 = types.count(2)
c3 = types.count(3)

if u > c1 + c3 or d > c2 + c3:
    print("NO")
    sys.exit(0)

res = [''] * n

need = u
for i in range(n):
    if need == 0:
        break
    if types[i] == 1:
        res[i] = 'U'
        need -= 1

for i in range(n):
    if need == 0:
        break
    if types[i] == 3 and res[i] == '':
        res[i] = 'U'
        need -= 1

need = d
for i in range(n):
    if need == 0:
        break
    if types[i] == 2 and res[i] == '':
        res[i] = 'D'
        need -= 1

for i in range(n):
    if need == 0:
        break
    if types[i] == 3 and res[i] == '':
        res[i] = 'D'
        need -= 1

if '' in res:
    print("NO")
else:
    print("YES")
    sys.stdout.write("".join(res))
