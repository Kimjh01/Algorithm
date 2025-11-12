T = int(input())

def coor(x, y):

    if x == 0 or y == 0:
        pass
    elif x > 0 and y > 0:
        arr[1] += 1
    
    elif x < 0 and y > 0:
        arr[2] += 1
    
    elif x < 0 and y < 0:
        arr[3] += 1
    
    elif x > 0 and y < 0:
        arr[4] += 1

arr = [0] * (5)

for _ in range(T):
    x, y = map(int, input().split())
    coor(x, y)

for i in range(1, 5):
    print(f'Q{i}: {arr[i]}')

print('AXIS:', 5 - arr.count(0))