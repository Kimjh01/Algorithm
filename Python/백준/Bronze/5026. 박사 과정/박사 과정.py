N = int(input())
for _ in range(N):
    eq = input()
    if eq != "P=NP":
        print(eval(eq))
    else:
        print("skipped")