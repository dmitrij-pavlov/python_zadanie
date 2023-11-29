n = int(input())
names = []
search = []
for i in range(n):
    names.append(input())
search_num = int(input())
for i in range(search_num):
    search.append(input())
for i in names:
    rt = True
    for j in search:
        if j not in i:
            rt = False
    if rt:
        print(i)
