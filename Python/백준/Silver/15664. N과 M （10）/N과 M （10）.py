from itertools import combinations

N, M = map(int, input().split())

arr = sorted(list(map(int, input().split())))

result = sorted(list(set(combinations(arr, M))))

for row in result:
    print(*row)