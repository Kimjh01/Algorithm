import sys
input = sys.stdin.readline

T = int(input().strip())
queries = [int(input().strip()) for _ in range(T)]
maxN = max(queries)


P = [0] * (maxN + 1)

base = [0, 1, 1, 1, 2, 2]  
for i in range(1, min(maxN, 5) + 1):
    P[i] = base[i]

for i in range(6, maxN + 1):
    P[i] = P[i - 1] + P[i - 5]

print("\n".join(str(P[n]) for n in queries))