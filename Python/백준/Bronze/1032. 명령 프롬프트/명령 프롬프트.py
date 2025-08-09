import sys

N = int(sys.stdin.readline().strip())
names = [sys.stdin.readline().strip() for _ in range(N)]

pattern = list(names[0])
for i in range(len(pattern)):
    for j in range(1, N):
        if names[j][i] != pattern[i]:
            pattern[i] = '?'
            break

print(''.join(pattern))