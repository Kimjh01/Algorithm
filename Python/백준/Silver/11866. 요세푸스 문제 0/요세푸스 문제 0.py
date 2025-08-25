N, K= map(int,input().split())
arr=[]
for i in range(N):
    arr.append(i+1)

result=[]
now=K-1
i = sum(arr)
while i>=0:
    if len(arr)==1:
        result.append(arr.pop())
        break
    result.append(arr.pop(now))
    now=(now+K-1)%len(arr)
    i = sum(arr)
    

result=', '.join(map(str,result))
print(f'<{result}>')