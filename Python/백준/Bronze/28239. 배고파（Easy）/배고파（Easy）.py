import sys

n = int(sys.stdin.readline())
for _ in range(n):
    m = int(sys.stdin.readline())
    rev_bin = bin(m)[2:][::-1]
    bits = [i for i, b in enumerate(rev_bin) if b == '1']
    
    if len(bits) == 1:
        print(bits[0] - 1, bits[0] - 1)
    else:
        print(bits[0], bits[1])