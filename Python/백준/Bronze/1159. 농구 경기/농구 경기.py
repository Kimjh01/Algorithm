import sys
from collections import Counter

input = sys.stdin.readline

n = int(input().strip())
c = Counter()

for _ in range(n):
    name = input().strip()
    if name:
        c[name[0].lower()] += 1

ans = ''.join(ch for ch in sorted(c) if c[ch] >= 5 and ch.isalpha())
print(ans if ans else "PREDAJA")