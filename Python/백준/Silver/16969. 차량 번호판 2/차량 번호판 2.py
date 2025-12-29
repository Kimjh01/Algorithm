import sys

s = sys.stdin.readline().strip()
mod = 1000000009
ans = 1

for i in range(len(s)):
    if s[i] == 'c':
        cnt = 26
    else:
        cnt = 10
    
    if i > 0 and s[i] == s[i-1]:
        cnt -= 1
        
    ans = (ans * cnt) % mod

print(ans)