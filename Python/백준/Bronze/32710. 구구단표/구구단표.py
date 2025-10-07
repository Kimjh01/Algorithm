n = int(input())

ok = False
if 1 <= n <= 9:
    ok = True
else:
    for a in range(2, 10):
        if n % a == 0 and n // a <= 9:
            ok = True
            break

print(1 if ok else 0)
