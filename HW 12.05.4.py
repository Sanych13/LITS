w = input('Ввести слова: ')


def percentage(x):
    b = 0
    s = 0
    for i in w:
        if i.isupper() and i.isspace() == False:
            b += 1
        elif i.islower() and i.isspace() == False:
            s += 1
    print("Відсоток великих букв = ", (b / (b + s)) * 100, "%")
    print("Відсоток малих букв = ", (s / (b + s)) * 100, "%")


print(percentage(w))
