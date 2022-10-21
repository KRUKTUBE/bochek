print("Войдите в профиль")
while True:
    l=input("Введите логин: ")
    if l == "lyaha":
        print("Логин найден!")
    else:
        print("Не верно! Попробуйте ещё раз")
    p=input("Введите пароль: ")
    if p == "lyashka":
        print("Пароль верный!")
    else:
        print("Не верно! Введите ещё раз")
    if l == "lyaha" and p == "lyashka":
        print("Успешный вход!")
        break
    else:
        print("Логин неверный")