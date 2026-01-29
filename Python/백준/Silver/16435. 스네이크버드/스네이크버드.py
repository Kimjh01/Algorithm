n, l = map(int, input().split())
h = list(map(int, input().split()))
h.sort()
for x in h:
    if x <= l:
        l += 1
    else:
        break
        
print(l)
