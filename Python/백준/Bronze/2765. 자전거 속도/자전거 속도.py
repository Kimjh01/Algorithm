import sys
from math import pi

i = 1
while True:
    input = sys.stdin.readline()
    if not input: 
        break
    d, r, t = map(float, input.split())
    if r == 0: 
        break
    dist = (d * pi * r) / 63360
    mph = (dist / t) * 3600
    print(f"Trip #{i}: {dist:.2f} {mph:.2f}")
    i += 1