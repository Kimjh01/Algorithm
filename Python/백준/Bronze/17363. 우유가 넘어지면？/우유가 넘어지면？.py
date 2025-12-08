import sys

mapper = {
    '.': '.', 'O': 'O', '-': '|', '|': '-',
    '/': '\\', '\\': '/', '^': '<', '<': 'v', 
    'v': '>', '>': '^'
}

N, M = map(int, sys.stdin.readline().split())
arr = [sys.stdin.readline().strip() for _ in range(N)]

for j in range(M - 1, -1, -1):
    for i in range(N):
        print(mapper[arr[i][j]], end='')
    print()