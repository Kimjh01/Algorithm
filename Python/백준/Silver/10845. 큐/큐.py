from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
q = deque()

for _ in range(n):
    cmd = input().split()
    op = cmd[0]
    if op == 'push':
        q.append(int(cmd[1]))
    elif op == 'pop':
        print(q.popleft() if q else -1)
    elif op == 'size':
        print(len(q))
    elif op == 'empty':
        print(1 if not q else 0)
    elif op == 'front':
        print(q[0] if q else -1)
    elif op == 'back':
        print(q[-1] if q else -1)
