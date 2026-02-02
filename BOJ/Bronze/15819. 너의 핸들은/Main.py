data = input().split()
N, I = int(data[0]), int(data[1])

arr = []
for _ in range(N):
    arr.append(input())

arr.sort()
print(arr[I-1])