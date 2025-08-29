import sys
input = sys.stdin.readline

n = int(input())
stack = []
ops = []
cur = 1
possible = True

for _ in range(n):
    t = int(input())

    while cur <= t:
        stack.append(cur)
        ops.append('+')
        cur += 1

    if stack and stack[-1] == t:
        stack.pop()
        ops.append('-')
    else:
        possible = False
        break

if not possible:
    print("NO")
else:
    print('\n'.join(ops))
