word_1 = input()
minw = word_1
maxw = word_1
while True:
    word_2 = input()
    if word_2 == 'стоп':
        break
    if len(word_2) > len(maxw):
        maxw = word_2
    if len(word_2) < len(minw):
        minw = word_2

if len(set(minw) -  set(maxw)) == 0:
    print('Да')
else:
    print('Нет')