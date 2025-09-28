N = int(input().strip())
heights = list(map(int, input().split()))
cnt = 1
for i in range(N - 1):
    if heights[i] <= heights[i+1]:
        cnt += 1
print(cnt)
