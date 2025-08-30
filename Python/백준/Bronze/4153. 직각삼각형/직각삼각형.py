while True:
    line = list(map(int, input().split()))
    if line == [0, 0, 0]:
        break

    line = sorted(line)
    if (line[0]**2+line[1]**2) == line[2]**2:
        print('right')
    else:
        print('wrong')
