import sys
for line in sys.stdin:
    if not line.strip():
        continue
    a, b, c = map(int, line.split())
    print(max(b - a, c - b) - 1)
