arr = list(map(int, input().split()))
ans = 0
for i in range(len(arr)):
    ans += arr[i]**2
print(ans%10)