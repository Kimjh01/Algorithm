while True:
    s = input()
    if s == '.':
        break

    stack = []
    ok = True
    for ch in s:
        if ch == '(' or ch == '[':
            stack.append(ch)
        elif ch == ')':
            if not stack or stack[-1] != '(':
                ok = False
                break
            stack.pop()
        elif ch == ']':
            if not stack or stack[-1] != '[':
                ok = False
                break
            stack.pop()

    print('yes' if ok and not stack else 'no')
