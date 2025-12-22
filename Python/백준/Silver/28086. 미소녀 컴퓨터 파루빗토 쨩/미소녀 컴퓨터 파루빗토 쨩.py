import sys
import math

s = sys.stdin.readline().strip()

op_idx = -1
for i in range(1, len(s)):
    if s[i] in "+-*/":
        op_idx = i
        break
        
op = s[op_idx]
A_str = s[:op_idx]
B_str = s[op_idx+1:]

A = int(A_str, 8)
B = int(B_str, 8)

res = 0
error = False

if op == '+':
    res = A + B
elif op == '-':
    res = A - B
elif op == '*':
    res = A * B
elif op == '/':
    if B == 0:
        print("invalid")
        error = True
    else:
        res = math.floor(A / B)

if not error:
    if res < 0:
        print('-' + oct(res)[3:])
    else:
        print(oct(res)[2:])