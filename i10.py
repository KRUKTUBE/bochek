print("калькулятор")
while True:
    a1 = input("Введите операцию: ")
    a2 = int(input("Введите первое слагаемое: "))
    a3 = int(input("Введите второе слагаемое: "))
    if a1 == "+":
        print(a2 + a3)
    elif a1 == "-":
        print(a2 - a3)
    elif a1 == "*":
        print(a2 * a3)
    elif a1 == "/":
        print(a2 / a3)
