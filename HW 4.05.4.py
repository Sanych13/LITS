n = input("Розпочати роботу - y/n ")
while n!= "n":
        a = float(input("Ввести перше число:"))
        c = input("Введіть потрібну операцію:")
        b = float(input("Ввести друге число:"))
        if c == "+":
            x = a + b
            print("Результат: " + str(x))
            n = input("Продовжити роботу - y/n ")
        elif c == "-":
            x = a - b
            print("Результат: " + str(x))
            n = input("Продовжити роботу - y/n ")
        elif c == "*":
            x = a * b
            print("Результат: " + str(x))
            n = input("Продовжити роботу - y/n ")
        elif c == "/":
            x = a / b
            print("Результат: " + str(x))
            n = input("Продовжити роботу - y/n ")


