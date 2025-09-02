from itertools import permutations


N, M = map(int, input().split())

arr = sorted(list(map(int, input().split())))

result = list(permutations(arr, M))

for row in result:
    print(*row)