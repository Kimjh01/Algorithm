def fibo(n):	
	if n == 2 or n == 1:
		return 1
	elif n <= 0:
		return 0
	else:
		return fibo(n-1) + fibo(n-2)

N = int(input())
print(fibo(N)) 