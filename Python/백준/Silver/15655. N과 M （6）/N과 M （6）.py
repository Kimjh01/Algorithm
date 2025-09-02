from itertools import combinations


N, M = map(int, input().split())

arr = sorted(list(map(int, input().split())))

result = list(combinations(arr, M))

for row in result:
    print(*row)