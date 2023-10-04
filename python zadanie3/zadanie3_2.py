password1 = input("Введите пароль: ")
password2 = input("Подтвердите пароль: ")
if len(password1) < 8:
    print("короткий!")
else:
    if password1 != password2:
        print("различаются.")
    else:
        print("OK")
