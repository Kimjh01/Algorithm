N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
result = sum(a * b for a, b in zip(A, sorted(B, reverse=True)))
print(result)
