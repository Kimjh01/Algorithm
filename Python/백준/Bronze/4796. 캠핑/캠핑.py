case_num = 1

while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
        
    full = V // P     
    rest = V % P    
    ans = full * L + min(L, rest)

    print(f"Case {case_num}: {ans}")
    case_num += 1
