from itertools import permutations

N, M = map(int, input().split())

arr = [ _ for _ in range(1, N+1)]
result = list(permutations(arr, M))

for row in result:
    print(*row)