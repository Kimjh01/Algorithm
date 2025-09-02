from itertools import combinations_with_replacement

N, M = map(int, input().split())

arr = sorted(list(map(int, input().split())))

result = sorted(list(set(combinations_with_replacement(arr, M))))

for row in result:
    print(*row)
