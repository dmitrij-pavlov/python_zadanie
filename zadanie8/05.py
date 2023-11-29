n = int(input())
for i in range(n):
    text = input()
    if 'Не' or 'не' in text:
        print(text[3:])
    else:
        print(text)
