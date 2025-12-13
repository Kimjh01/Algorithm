import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
ans = 0
tmp = 0

for i in range(1, n):
    if arr[i] > arr[i-1]:
        tmp += arr[i] - arr[i-1]
    else:
        ans = max(ans, tmp)
        tmp = 0
ans = max(ans, tmp)
print(ans)