import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * (n + 1)
arr[0] = 1
arr[1] = 3

for i in range(2, n + 1):
    arr[i] = (arr[i-1] * 2 + arr[i-2]) % 9901

print(arr[n])