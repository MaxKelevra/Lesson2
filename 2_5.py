rating = int(input("Введите рейтинг: "))
my_list = [7, 4, 3, 2]
r = my_list.count(rating)
for el in my_list:
    if r > 0:
        i = my_list.index(rating)
        my_list.insert(i+r, rating)
        break
    else:
        if rating > el:
            j = my_list.index(el)
            my_list.insert(j, rating)
            break
        elif rating < my_list[len(my_list) - 1]:
            my_list.append(rating)
print("Текущий рейтинг: ", my_list)