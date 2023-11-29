n = int(input())
names = []
for i in range(n):
    names.append(input())
search = input()
for j in names:
    if search in j:
        print(j)
