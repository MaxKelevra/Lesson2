seasons_list = ["Winter", "Spring", "Summer", "Autumn"]
month = int(input("Введите номер месяца: "))
if month == 1 or month == 12 or month == 2:
    print(seasons_list[0])
elif month == 3 or month == 4 or month == 5:
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_list[2])
elif month == 9 or month == 10 or month == 11:
    print(seasons_list[3])
else:
    print("введите корректное число!")

#########################################################

season_dict = {1: 'Winter', 2: "Spring", 3: "Summer", 4: "Autumn"}
month = int(input("Введите номер месяца: "))
if month == 1 or month == 12 or month == 2:
    print(season_dict.get(1))
elif month == 3 or month == 4 or month == 5:
    print(season_dict.get(2))
elif month == 6 or month == 7 or month == 8:
    print(season_dict.get(3))
elif month == 9 or month == 10 or month == 11:
    print(season_dict(4))
else:
    print("Введите корректное число!")
