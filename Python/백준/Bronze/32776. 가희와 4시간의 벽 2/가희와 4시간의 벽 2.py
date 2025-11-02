S = int(input().strip())
Ma, F, Mb = map(int, input().split())

if S <= 240 or S <= Ma + F + Mb:
    print("high speed rail")
else:
    print("flight")
