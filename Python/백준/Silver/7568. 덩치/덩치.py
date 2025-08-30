n = int(input())
arr = [tuple(map(int, input().split())) for i in range(n)]

ranks = [1] * n
for i in range(n):
    for j in range(n):
        if i != j and arr[j][0] > arr[i][0] and arr[j][1] > arr[i][1]:
            ranks[i] += 1

print(*ranks)
