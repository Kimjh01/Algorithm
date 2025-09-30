import sys
N, r, c = map(int, sys.stdin.readline().split())

ans = 0
n = N
while n > 0:
    half = 1 << (n - 1)      
    block = half * half       
    if r < half and c < half:         
        pass
    elif r < half and c >= half:       
        ans += block * 1
        c -= half
    elif r >= half and c < half:       
        ans += block * 2
        r -= half
    else:                              
        ans += block * 3
        r -= half
        c -= half
    n -= 1

print(ans)
