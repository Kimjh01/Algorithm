N = int(input())

for _ in range(N):
    loop_num, word = map(str, input().split())
    for idx in range(len(word)):
        for _ in range(int(loop_num)):
            print(word[idx], end='')
    print()
    