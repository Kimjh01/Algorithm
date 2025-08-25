N = int(input())
words = {input().strip() for _ in range(N)}

words = sorted(words)          
words = sorted(words, key=len) 

for result in words:
    print(result)
