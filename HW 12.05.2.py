def d(l):
    new_l = []
    for i in l:
        if i.isdigit():
            new_l.append(i)
    print(new_l)


d('abc83 cde7 1 b 24')




# def d(l):
#     new_l = []
#     for i in str.split(l):
#         if i.isdigit():
#             new_l.append(i)
#     print(new_l)
#
#
# d('abc83 cde7 1 b 24')