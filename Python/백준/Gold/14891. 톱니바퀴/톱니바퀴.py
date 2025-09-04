magnets = [list(map(int, input().strip())) for _ in range(4)]
K = int(input())
rotations = [list(map(int, input().split())) for _ in range(K)]
 
for magnet_num, direction in rotations:
    magnet_num -= 1
    rotate_dir = [0] * 4
    rotate_dir[magnet_num] = direction
 
    for i in range(magnet_num, 3):
        if magnets[i][2] != magnets[i + 1][6]:
            rotate_dir[i + 1] = -rotate_dir[i]
        else:
            break
 
    for i in range(magnet_num, 0, -1):
        if magnets[i][6] != magnets[i - 1][2]:
            rotate_dir[i - 1] = -rotate_dir[i]
        else:
            break
    for i in range(4):
        if rotate_dir[i] == 1:
            magnets[i] = [magnets[i][-1]] + magnets[i][:-1]
        elif rotate_dir[i] == -1:
            magnets[i] = magnets[i][1:] + [magnets[i][0]]
 
    score = sum(magnets[i][0] * (2 ** i) for i in range(4))
print(score)