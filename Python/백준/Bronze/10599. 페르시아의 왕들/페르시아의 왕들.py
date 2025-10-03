import sys

def main():
    input = sys.stdin.readline
    while True:
        line = input().split()
        if not line:
            break
        a, b, c, d = map(int, line)
        if a == 0 and b == 0 and c == 0 and d == 0:
            break
        min_age = c - b
        max_age = d - a
        print(min_age, max_age)

if __name__ == "__main__":
    main()
