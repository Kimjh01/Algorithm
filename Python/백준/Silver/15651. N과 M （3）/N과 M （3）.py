from itertools import product

N, M = map(int, input().split())

arr = [ _ for _ in range(1, N+1)]
result = list(product(arr, repeat=M))

for row in result:
    print(*row)