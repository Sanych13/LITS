def s(a, b, c):
    p = (a + b + c) / 2
    t = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return t


print(s(6, 2, 3))
