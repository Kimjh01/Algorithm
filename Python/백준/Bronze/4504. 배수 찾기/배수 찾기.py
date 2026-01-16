import sys
input = sys.stdin.readline

n = int(input())

while True:
    t = int(input())
    if t == 0:
        break
    
    if t % n == 0:
        print(f"{t} is a multiple of {n}.")
    else:
        print(f"{t} is NOT a multiple of {n}.")