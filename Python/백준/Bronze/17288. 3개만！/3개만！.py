s = input().strip()

cnt = 0
length = 1 

for i in range(1, len(s)):
    if ord(s[i]) == ord(s[i-1]) + 1:
        length += 1
    else:
        if length == 3:
            cnt += 1
        length = 1  

if length == 3:
    cnt += 1

print(cnt)
