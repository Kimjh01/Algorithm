A, B, C, D, E = map(int, input().split())
    
basket = 0
basket += E
basket += D

if A <= D:
    A = 0
else:
    A -= D

basket += C
if B >= C:
    B -= C
    basket += B // 2 + (B % 2)
    A -= B // 2
    if B % 2:
        A -= 3
else:
    C -= B
    A -= C * 2

if A > 0:
    basket += A // 5
    if A % 5:
        basket += 1

print(basket)
