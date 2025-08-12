n = int(input().strip())
covered = set()

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            covered.add((i, j))

print(len(covered))
