import sys
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
S = input().strip()

ans = 0
cnt = 0
i = 0
while i + 2 < M:
    if S[i] == 'I' and S[i+1] == 'O' and S[i+2] == 'I':
        cnt += 1
        if cnt >= N:
            ans += 1     
        i += 2          
    else:
        cnt = 0
        i += 1

print(ans)
