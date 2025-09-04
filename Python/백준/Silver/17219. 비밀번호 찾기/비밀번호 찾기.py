N, M = map(int, input().split())

web_list_dict = {}
for _ in range(N):
    idx, value = map(str, input().split())
    web_list_dict[idx] = value

for i in range(M):
    web_site = input()
    print(web_list_dict[web_site])
