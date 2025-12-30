import sys

n = int(sys.stdin.readline())
items = []
for _ in range(n):
    items.append(list(map(int, sys.stdin.readline().split())))

items.sort(key=lambda x: (-x[0], x[1]))
print(items[0][0], items[0][1], items[1][0], items[1][1])

items.sort(key=lambda x: (x[1], -x[0]))
print(items[0][0], items[0][1], items[1][0], items[1][1])