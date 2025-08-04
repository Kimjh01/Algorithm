N = int(input())

for _ in range(N):
    vps = input()
    stack = []
    is_valid = True
    
    for ch in vps:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if stack:
                stack.pop()
            else:
                is_valid = False
                break
    
    if stack:
        is_valid = False

    print("YES" if is_valid else "NO")