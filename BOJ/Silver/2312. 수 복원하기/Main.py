import sys

input = sys.stdin.readline
t = int(input().strip())
out = []
for _ in range(t):
    n = int(input().strip())
    p = 2
    while p * p <= n:
        if n % p == 0:
            c = 0
            while n % p == 0:
                n //= p
                c += 1
            out.append(f"{p} {c}")
        p += 1 if p == 2 else 2
    if n > 1:
        out.append(f"{n} 1")
sys.stdout.write("\n".join(out))
