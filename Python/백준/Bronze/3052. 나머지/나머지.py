result = []
for i in range(10):
    A = int(input())
    result.append(A%42)

print(len(set(result)))