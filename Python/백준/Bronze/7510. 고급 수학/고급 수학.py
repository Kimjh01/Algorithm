import sys

t = int(sys.stdin.readline())
for i in range(1, t + 1):
    a, b, c = sorted(map(int, sys.stdin.readline().split()))
    print(f"Scenario #{i}:")
    if a * a + b * b == c * c:
        print("yes")
    else:
        print("no")
    if i != t:
        print()
