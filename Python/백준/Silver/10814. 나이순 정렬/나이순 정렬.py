N = int(input())
arr = []
for i in range(N):
    age, name = input().split()
    age = int(age)
    arr.append((age, name))

arr.sort(key=lambda x: x[0])

for age, name in arr:
    print(age, name)
