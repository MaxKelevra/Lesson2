el = input("Введите элементы списка: ").split()
el[:-1:2], el[1::2] = el[1::2], el[:-1:2]
print(el)