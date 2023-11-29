n = int(input())
count = 0
for i in range(n):
    text = input()
    if '%' in text[0]:
        for j in text:
            if j == '%':
                count += 1
        print(text[count:])
        count = 0
    elif '#' in text[0]:
        continue
    else:
        print(text)
