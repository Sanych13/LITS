a = input("Ввести число: ")
paired = 0
unpaired = 0
for i in a:
    if int(i) % 2 == 0:
        paired += 1
    elif int(i) % 2 != 0:
        unpaired += 1
print('парних - ' + str(paired))
print('непарних - ' + str(unpaired))

