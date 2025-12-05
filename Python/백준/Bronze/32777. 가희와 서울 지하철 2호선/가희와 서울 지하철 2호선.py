import sys
input = sys.stdin.readline

TOTAL_STATIONS = 43

Q = int(input())

for _ in range(Q):
    A, B = map(int, input().split())
    start = A - 201
    end = B - 201

    inner_dist = (end - start + TOTAL_STATIONS) % TOTAL_STATIONS

    outer_dist = TOTAL_STATIONS - inner_dist

    if inner_dist < outer_dist:
        print("Inner circle line")
    elif outer_dist < inner_dist:
        print("Outer circle line")
    else:
        print("Same")