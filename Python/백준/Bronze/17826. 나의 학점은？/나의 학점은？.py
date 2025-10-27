N = list(map(int, input().split()))
target = int(input())
N.sort(reverse=True)
num = N.index(target) + 1
if num <= 5:
    print("A+")
elif num <= 15:
    print("A0")
elif num <= 30:
    print("B+")
elif num <= 35:
    print("B0")
elif num <= 45:
    print("C+")
elif num <= 48:
    print("C0")
elif num <= 50:
    print("F")