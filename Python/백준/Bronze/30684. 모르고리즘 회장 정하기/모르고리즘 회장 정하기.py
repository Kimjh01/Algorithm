N = int(input())
name = []
for _ in range(N):
    temp = str(input())
    if len(temp) == 3:
        name.append(temp)
name.sort()
print(name[0])

