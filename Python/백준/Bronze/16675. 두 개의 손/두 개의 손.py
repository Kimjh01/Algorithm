idx = {c: i for i, c in enumerate("SRP")}
ML, MR, TL, TR = (idx[x] for x in input().split())

if ML == MR and (ML + 1) % 3 in (TL, TR):
    print("TK")
elif TL == TR and (TL + 1) % 3 in (ML, MR):
    print("MS")
else:
    print("?")
