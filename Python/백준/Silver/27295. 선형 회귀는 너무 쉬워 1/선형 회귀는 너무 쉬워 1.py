import sys
import math
input = sys.stdin.readline

n, b = map(int, input().split())
sum_y_minus_b = 0
sum_x = 0

for _ in range(n):
    x, y = map(int, input().split())
    sum_y_minus_b += (y - b)
    sum_x += x

if sum_x == 0:
    print("EZPZ")
else:
    g = math.gcd(abs(sum_y_minus_b), abs(sum_x))
    num = sum_y_minus_b // g
    den = sum_x // g
    
    if den < 0:
        num, den = -num, -den
    
    if num % den == 0:
        print(num // den)
    else:
        print(f"{num}/{den}")