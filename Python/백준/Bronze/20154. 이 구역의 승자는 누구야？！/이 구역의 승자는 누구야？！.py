s = input().strip()

stroke_str = "32123333113133122212112221"
strokes = {chr(ord('A') + i): int(stroke_str[i]) for i in range(26)}

total = sum(strokes[ch] for ch in s)

if total % 2 == 1:
    print("I'm a winner!")
else:
    print("You're the winner?")
