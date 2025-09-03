while True:
    try:
        n = int(input())
    except EOFError:   
        break

    seen = set()
    k = 0
    while len(seen) < 10:
        k += 1
        val = n * k
        for ch in str(val):
            seen.add(ch)

    print(k)