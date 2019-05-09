a = int(input('Ввести число: '))
x = 0
while a > 0:
    x = x*10 + a % 10
    a = a//10
print(x)
