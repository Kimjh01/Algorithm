n, k = map(int, input().split())
k = min(k, n-k)  
num = und = 1
for i in range(1, k+1):
    num *= n - (i - 1)
    und *= i
print(num // und)