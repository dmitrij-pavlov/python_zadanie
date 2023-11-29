n = int(input())
text = []
for i in range(n):
    text.append(input())
index = int(input())
for j in text:
    if index > len(j):
        continue
    else:
        print(j[index - 1], end='')
