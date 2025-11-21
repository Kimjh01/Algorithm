arr = [list(input().strip()) for _ in range(5)]  
res = []

for i in range(max(len(row) for row in arr)):  
    for j in range(5):
        if i < len(arr[j]): 
            res.append(arr[j][i])

print("".join(res))