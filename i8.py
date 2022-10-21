import random
print("угадай число от 1 до 10")
q = random.randint(1, 10)
while True:
    a = int(input("Число: "))
    if a == q:
        print("молодец")
        break
    if a >= q:
        print("возьми поменьше")
    if a <= q:
        print("возьми побольше")
