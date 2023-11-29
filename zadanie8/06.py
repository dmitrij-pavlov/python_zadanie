max_len = int(input())
n = int(input())
for i in range(n):
    word = input()
    if len(word) > max_len:
        print(word[:max_len - 3], end='...')
    else:
        print(word)