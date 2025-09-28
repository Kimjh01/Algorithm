N = int(input().strip())
s = input().strip()

codes = ["000000","001111","010011","011100","100110","101001","110101","111010"]
letters = "ABCDEFGH"

ans = []
for i in range(N):
    block = s[6*i:6*i+6]
    found = None
    for idx, code in enumerate(codes):
        diff = sum(block[j] != code[j] for j in range(6))
        if diff <= 1:
            found = letters[idx]
            break
    if not found:
        print(i + 1)
        raise SystemExit
    ans.append(found)

print("".join(ans))
