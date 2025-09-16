A, B = map(int, input().split())
C = int(input())
D = A + B
E = 0 
if C != 0 and D != 0:
    E = D // C

if E <= 1 or D == 0:
    ans = D
else:
    ans = D - 2*C

print(ans)