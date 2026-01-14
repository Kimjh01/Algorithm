s = input()
N = len(s)
ans = 0

for length in range(N, 0, -1):
    if length % 2 != 0:
        continue
    
    half = length // 2
    found = False
    
    for i in range(N - length + 1):
        left_sub = s[i : i + half]
        right_sub = s[i + half : i + length]
        
        sum_l = 0
        sum_r = 0
        
        for c in left_sub: sum_l += int(c)
        for c in right_sub: sum_r += int(c)
        
        if sum_l == sum_r:
            ans = length
            found = True
            break
            
    if found:
        break

print(ans)