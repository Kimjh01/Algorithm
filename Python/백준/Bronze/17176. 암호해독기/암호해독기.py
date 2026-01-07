import sys

def solve():
    n = int(sys.stdin.readline())
    cipher_nums = list(map(int, sys.stdin.readline().split()))
    plain_text = sys.stdin.readline().rstrip('\n')

    count = [0] * 53
    for num in cipher_nums:
        count[num] += 1

    for char in plain_text:
        if char == ' ':
            target = 0
        elif 'A' <= char <= 'Z':
            target = ord(char) - ord('A') + 1
        elif 'a' <= char <= 'z':
            target = ord(char) - ord('a') + 27
        
        count[target] -= 1
        
        if count[target] < 0:
            print("n")
            return

    print("y")

solve()