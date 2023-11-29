n = int(input())

for i in range(n):
    word = input()
    if 'кот' in word:
        for j in range(len(word)):
            if word[j] == 'к':
                print(i + 1, j + 1)
