print("Войдите в профиль")
while True:
    l=input("Введите логин: ")
    p=input("Введите пароль: ")
    if l == "moshka" and p == "bobka":
        print("Успешный вход")
        break
    else:
        print("Не верно! Введите ещё раз")
