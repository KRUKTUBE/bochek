print("Бонусы")
m = 0
b = 0
while m<1001:
    m = int(input("Введите число: "))
    m = m / 10
    b = b + m
    print(b)
    if b >= 1000:
        print("пора тратить бонусы!")
        break
    else:
        print("дальше")
