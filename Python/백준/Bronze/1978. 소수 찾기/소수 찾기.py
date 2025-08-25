N = int(input())
nums = list(map(int, input().split()))

def is_prime(x):
    if x < 2:
        return False
    if x in (2, 3):
        return True
    if x % 2 == 0:
        return False
    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2
    return True

print(sum(1 for v in nums if is_prime(v)))
