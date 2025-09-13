import sys

input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    n = int(input().strip())
    kinds = {} 
    for _ in range(n):
        name, kind = input().split()
        if kind not in kinds:
            kinds[kind] = 0
        kinds[kind] += 1

    result = 1
    for cnt in kinds.values():
        result *= (cnt + 1)
    print(result - 1)
