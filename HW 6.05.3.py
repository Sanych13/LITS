def vr(y):
    if y != 100 and y % 4 == 0 and y % 400 == 0:
        return True
    else:
        return False


print(vr(2000))
