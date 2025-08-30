n = int(input())
cnt = 0
while n:
    n //= 5
    cnt += n
print(cnt)
