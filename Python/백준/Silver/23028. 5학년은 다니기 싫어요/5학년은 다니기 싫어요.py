import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())

n = 8 - n
need_major = 66 - a
need_total = 130 - b

semesters = [list(map(int, input().split())) for _ in range(10)]
semesters = semesters[:n]

max_major = 0
for maj, non in semesters:
    max_major += maj * 3

if max_major < need_major:
    print("Nae ga wae")
else:
    max_total = 0
    for maj, non in semesters:
        courses = maj + non
        if courses > 6:
            courses = 6
        max_total += courses * 3

    if max_total >= need_total:
        print("Nice")
    else:
        print("Nae ga wae")
