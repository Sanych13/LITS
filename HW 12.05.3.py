def words(w):
    l = len(w)
    for i in range(l):
        for t in range(i + 1, l):
            if len(w[i]) > len(w[t]):
                temp = w[i]
                w[i] = w[t]
                w[t] = temp
    return len(w[0])


print(words(['fghjfg', 'hj', 'jjj']))
