arr = [0 for _ in range(10)]
temp = 1
for _ in range(3):
    temp *= int(input())

temp = str(temp)
for i in range(len(temp)):
    arr[int(temp[i])] += 1
    
for i in range(10):
    print(arr[i])