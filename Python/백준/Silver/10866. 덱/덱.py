from collections import deque
d = deque()
n = int(input())
out = []

for _ in range(n):
    cmd = input().split()

    if cmd[0] == 'push_front':
        d.appendleft(int(cmd[1]))
    elif cmd[0] == 'push_back':
        d.append(int(cmd[1]))
    elif cmd[0] == 'pop_front':
        out.append(str(d.popleft() if d else -1))
    elif cmd[0] == 'pop_back':
        out.append(str(d.pop() if d else -1))
    elif cmd[0] == 'size':
        out.append(str(len(d)))
    elif cmd[0] == 'empty':
        out.append('0' if d else '1')
    elif cmd[0] == 'front':
        out.append(str(d[0] if d else -1))
    elif cmd[0] == 'back':
        out.append(str(d[-1] if d else -1))

print('\n'.join(out))
