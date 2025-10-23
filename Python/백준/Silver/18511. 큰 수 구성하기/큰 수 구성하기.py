from itertools import product

target, num = map(int, input().split())
arr = list(map(int, input().split()))

ans = -1
for length in range(len(str(target)), 0, -1):
    for temp in product(arr, repeat=length):
        res = int("".join(map(str, temp)))
        if target >= res:
            ans = max(ans, res)

print(ans) 