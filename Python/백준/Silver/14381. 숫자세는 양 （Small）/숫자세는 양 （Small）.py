import sys
input = sys.stdin.readline

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    if N == 0:
        print(f"Case #{t}: INSOMNIA")
        continue

    seen = set()
    current = 0
    i = 1
    while len(seen) < 10:
        current = N * i
        for s in str(current):
            seen.add(s)
        i += 1
    
    print(f"Case #{t}: {current}")