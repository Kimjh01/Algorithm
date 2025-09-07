N, M = map(int, input().split())
listen = []
look = []
for _ in range(N):
    listen.append(input())

for _ in range(M):
    look.append(input())

result = sorted(list(set(look) & set(listen)))
print(len(result))
for row in range(len(result)):
    print(result[row])