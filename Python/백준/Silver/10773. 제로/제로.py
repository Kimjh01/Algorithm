import sys
input = sys.stdin.readline

n = int(input())
stack = []
ops = []

for _ in range(n):

    t = int(input())

    if stack and 0 == t:
        stack.pop()
    else:
        stack.append(t)


print(sum(stack))
