import sys
input = sys.stdin.readline

def binary_search(array, target):
    left, right = 0, len(array)-1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return True
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

N = int(input())
numbers_1 = sorted(list(map(int, input().split())))

M = int(input())
numbers_2 = list(map(int, input().split()))

for num in numbers_2:
    print(1 if binary_search(numbers_1, num) else 0)
