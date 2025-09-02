from itertools import combinations_with_replacement


N, M = map(int, input().split())

arr = [ _ for _ in range(1, N+1)]
result = list(combinations_with_replacement(arr, M))

for row in result:
    print(*row)
