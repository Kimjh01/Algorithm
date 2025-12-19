import sys

data = sys.stdin.read().split()

if data:
    B = data[-1]
    A = data[:-1]
    
    count = 0
    
    for phone in A:
        if phone != B and phone.startswith(B):
            count += 1
            
    print(count)