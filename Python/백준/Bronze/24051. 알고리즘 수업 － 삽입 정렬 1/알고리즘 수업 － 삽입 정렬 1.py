import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
K = int(data[1])
A = list(map(int, data[2:]))

count = 0

for i in range(1, N):
    loc = i - 1
    newItem = A[i]
    
    while 0 <= loc and newItem < A[loc]:
        A[loc + 1] = A[loc]
        count += 1
        if count == K:
            print(A[loc + 1])
            sys.exit()
        loc -= 1
    
    if loc + 1 != i:
        A[loc + 1] = newItem
        count += 1
        if count == K:
            print(A[loc + 1])
            sys.exit()

print(-1)