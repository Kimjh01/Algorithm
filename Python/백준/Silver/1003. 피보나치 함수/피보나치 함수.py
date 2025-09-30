import sys
input = sys.stdin.readline

T = int(input())
nums = [int(input()) for _ in range(T)]
M = max(nums) if nums else 0

cnt0 = [0]*(max(2, M+1))
cnt1 = [0]*(max(2, M+1))
cnt0[0], cnt1[0] = 1, 0
cnt0[1], cnt1[1] = 0, 1

for i in range(2, M+1):
    cnt0[i] = cnt0[i-1] + cnt0[i-2]
    cnt1[i] = cnt1[i-1] + cnt1[i-2]

for n in nums:
    print(cnt0[n], cnt1[n])
