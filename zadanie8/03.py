a = input()
for i in a:
    if i not in '1234567890_AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz':
        print('Неверный символ:', i)
        break
else:
    print('OK')