import sys

_ = sys.stdin.readline()

cnt = 0
for line in sys.stdin:
    s = line.strip()
    if s == "고무오리 디버깅 끝":
        break
    if s == "문제":
        cnt += 1
    elif s == "고무오리":
        if cnt == 0:
            cnt += 2
        else:
            cnt -= 1

print("고무오리야 사랑해" if cnt == 0 else "힝구")
