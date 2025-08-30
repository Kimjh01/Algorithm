s = input().strip()

target = s.index('*')

S = 0
for i, c in enumerate(s):
    if c == '*':
        continue
        
    d = int(c)
    
    if i % 2 == 0:
        w = 1 
    else:
        w = 3
        
    S += d * w

w = 1 if target % 2 == 0 else 3

for x in range(10):
    if (S + w * x) % 10 == 0:
        print(x)
        break
