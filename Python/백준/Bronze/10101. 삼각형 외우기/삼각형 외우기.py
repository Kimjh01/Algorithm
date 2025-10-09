a = int(input().strip())
b = int(input().strip())
c = int(input().strip())

if a + b + c != 180:
    print("Error")
elif a == b == c == 60:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")
