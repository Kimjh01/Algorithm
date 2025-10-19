color = {
    "black": (0, 0),
    "brown": (1, 1),
    "red": (2, 2),
    "orange": (3, 3),
    "yellow": (4, 4),
    "green": (5, 5),
    "blue": (6, 6),
    "violet": (7, 7),
    "grey": (8, 8),
    "white": (9, 9),
}
a = input().strip()
b = input().strip()
c = input().strip()
val = color[a][0] * 10 + color[b][0]
mul = color[c][1]
print(val * (10 ** mul))
