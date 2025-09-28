N = int(input().strip())
s = int(input().strip())
if N > 5:
    print("Love is open door")
else:
    for i in range(1, N):
        print((s + i) % 2)
