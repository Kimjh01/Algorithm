from itertools import product

N, M = map(int, input().split())

arr = sorted(list(map(int, input().split())))

result = list(product(arr, repeat=M))

for row in result:
    print(*row)