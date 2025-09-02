from itertools import permutations

N, M = map(int, input().split())

arr = list(map(int, input().split()))

result = sorted(list(set(permutations(arr, M))))

for row in result:
    print(*row)