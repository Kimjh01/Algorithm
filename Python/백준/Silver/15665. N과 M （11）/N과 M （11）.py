from itertools import product

N, M = map(int, input().split())

arr = sorted(list(map(int, input().split())))

result = sorted(list(set(product(arr, repeat=M))))

for row in result:
    print(*row)