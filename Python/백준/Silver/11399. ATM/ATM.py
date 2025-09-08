N = int(input())
arr = sorted(list(map(int, input().split())))
cnt = 0
temp = N
for i in range(N):
    cnt += arr[i] * (N-i)

print(cnt)