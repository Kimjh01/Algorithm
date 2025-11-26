import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    parts = input().split()
    n = int(parts[0])
    d, a, b, f = map(float, parts[1:])
    time = d / (a + b)
    dist = time * f
    print(f"{n} {dist:.6f}")
