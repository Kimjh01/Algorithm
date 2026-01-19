import sys

input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    a, b = map(int, input().split())
    arr.append(b - a)

arr.sort()

if n % 2 == 1:
    print(1)
else:
    print(arr[n // 2] - arr[n // 2 - 1] + 1)