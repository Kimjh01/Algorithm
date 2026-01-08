import sys
input = sys.stdin.read().split()
n = int(input[0])
m = input[1]
k = int(input[2])

if '1' not in m:
    print("YES")
else:
    if k == 0:
        print("YES")
    elif k >= n:
        print("NO")
    else:
        if '1' in m[n-k:]:
            print("NO")
        else:
            print("YES")