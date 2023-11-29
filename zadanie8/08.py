text = input()
orel = 0
max_len = 0
for i in text:
    if i == 'о':
        orel += 1
        max_len = orel
    if i == 'р':
        orel = 0
print(max_len)
