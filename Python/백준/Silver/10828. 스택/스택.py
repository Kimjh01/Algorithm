import sys
input = sys.stdin.readline
stack = []
for _ in range(int(input())):
    cmd = input().split()
    if cmd[0] == 'push':
        stack.append(cmd[1])
    elif cmd[0] == 'pop':
        print(stack.pop() if stack else -1)
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        print(0 if stack else 1)
    elif cmd[0] == 'top':
        print(stack[-1] if stack else -1)
