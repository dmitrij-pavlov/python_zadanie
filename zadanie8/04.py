n = int(input())
for j in range(n, 0, -1):
    print('', end='\n')
    for i in range(n):
        print(chr(ord('A') + i), ' ', sep=str(j), end='')