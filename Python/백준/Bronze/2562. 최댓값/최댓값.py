num=[]
for i in range(9):
    num.append(int(input()))
        
temp = max(num)
print(temp)
print(num.index(temp)+1)