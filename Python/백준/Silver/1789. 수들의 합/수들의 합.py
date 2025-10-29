S = int(input())
num = 0
max_cnt = 0
while True:
    num += 1
    max_cnt += num
    if S < max_cnt:
        print(num-1)
        break