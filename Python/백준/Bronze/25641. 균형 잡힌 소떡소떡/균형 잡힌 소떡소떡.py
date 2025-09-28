n = int(input().strip())
s = input().strip()

cnt_s = s.count('s')
cnt_t = s.count('t')

i = 0
while cnt_s != cnt_t:
    if s[i] == 's':
        cnt_s -= 1
    else:
        cnt_t -= 1
    i += 1

print(s[i:])
