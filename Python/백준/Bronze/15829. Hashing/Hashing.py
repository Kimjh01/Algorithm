M = 1234567891
r = 31

n = int(input())
s = input().strip()

nums = [ord(ch) - 96 for ch in s]

ans = 0
for i in range(n):
    ans = (ans + nums[i] * pow(r, i, M)) % M

print(ans)
