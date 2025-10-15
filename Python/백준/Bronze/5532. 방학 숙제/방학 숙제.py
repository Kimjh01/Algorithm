import math
L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
Homework = max(math.ceil(B/D),math.ceil(A/C))
print(L-Homework)