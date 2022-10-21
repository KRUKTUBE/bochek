print("Войдите в профиль")
while True:
    l=input("Введите логин: ")
    p=input("Введите пароль: ")
    if l == "lyaha" and p == "lyashka":
        print("Успешный вход!")
        break
    else:
        print("логин или пароль неверный")