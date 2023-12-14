n = int(input())
for i in range(n):
    text = input()
    if 'кот' in text:
        print(f"{i + 1} {text.find('кот')}")
