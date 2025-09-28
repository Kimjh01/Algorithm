A, B = input().split()

i, j, carry = len(A) - 1, len(B) - 1, 0
res = []

while i >= 0 or j >= 0 or carry:
    x = ord(A[i]) - 48 if i >= 0 else 0
    y = ord(B[j]) - 48 if j >= 0 else 0
    s = x + y + carry
    res.append(str(s & 1))
    carry = s >> 1
    i -= 1; j -= 1

r = ''.join(reversed(res)).lstrip('0')
print(r if r else '0')
