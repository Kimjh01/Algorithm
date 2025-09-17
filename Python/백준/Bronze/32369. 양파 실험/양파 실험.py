N, A, B = map(int, input().split())
O1, O2 = 1, 1
for i in range(N):
    O1 += A
    O2 += B
    if O1 == O2:
        O2 -= 1
    if O1 < O2:
        O1, O2 = O2, O1
        
print(O1, O2)