n = input()

while n != '0':
    for i in range(len(n)):
        if n[i] != n[-1*(i+1)]:
            print('no')
            break
        elif i == len(n)-1:
            print('yes')

    n = input()