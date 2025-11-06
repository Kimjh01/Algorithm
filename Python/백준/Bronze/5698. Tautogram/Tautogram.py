while True:

    N = input().split()

    if N[0] == '*':
        break

    ck = list(N[0].capitalize())
    ck = ck[0]

    for i in range(1, len(N)):
        temp = list(N[i].capitalize())
        temp = temp[0]
        if ck != temp:
            print('N')
            break 
    else:
        print('Y')