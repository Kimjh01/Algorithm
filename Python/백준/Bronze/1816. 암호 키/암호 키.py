import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    S = int(input())
    is_valid = True
    
    for i in range(2, 1000001):
        if S % i == 0:
            is_valid = False
            break
            
    if is_valid:
        print("YES")
    else:
        print("NO")