N = int(input().strip())
best_seq = []

for second in range(1, N + 1):
    seq = [N, second]
    while True:
        nxt = seq[-2] - seq[-1]
        if nxt < 0:
            break
        seq.append(nxt)
    if len(seq) > len(best_seq):
        best_seq = seq

print(len(best_seq))
print(*best_seq)
