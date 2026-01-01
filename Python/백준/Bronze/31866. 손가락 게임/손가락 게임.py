a, b = map(int, input().split())
v = [0, 2, 5]
if a not in v and b not in v:
    print("=")
elif a not in v:
    print("<")
elif b not in v:
    print(">")
elif a == b:
    print("=")
elif (a == 0 and b == 2) or (a == 2 and b == 5) or (a == 5 and b == 0):
    print(">")
else:
    print("<")