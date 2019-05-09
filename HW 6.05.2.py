def tf(a, b, c=0):
    d = (a, b, c)
    test = sorted(d)
    if test[2] >= test[0] + test[1]:
        return False
    elif len(d) != 3:
        return False
    else:
        return True


print(tf(5, 10, 15))

