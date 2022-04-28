"""1. Если переменная key равна 10,
выведите "Верно", если другому значению,
выведите "Не верно"
"""
# key = int(input('Enter your key'))
# if key == 10:
#     print('Верно')
# else:
#     print('Не верно')

"""2. Переменная num может принимать 4
значения: 1, 2, 3 или 4. Если она
имеет значение '1', то в переменную
result запишем 'зима', если имеет
значение '2' – 'весна' и так далее.
Если значения не 1,2,3,4, то вывести
"Нет такой поры года" и завершить
программу
"""
# num = int(input('Enter num')) # можно брать из консоли
# num_1 = list(range(1,5))
# result = ""
# # здесь логику
#
# if num == 1:
#     result = 'зима'
#     print(result.capitalize())
# elif num == 2:
#     result = 'весна'
#     print(result.capitalize())
# elif num == 3:
#     result = 'лето'
#     print(result.capitalize())
# elif num == 4:
#     result = 'осень'
#     print(result.capitalize())
# else:
#     print('Нет такой поры года')

"""3. В переменной month лежит какое-то
число из интервала от 1 до 12. Определите
в какую пору года попадает этот месяц
(зима, лето, весна, осень). Если число
меньше 1, то выведите "значение слишком
маленькое", если больше 12, "значение слишком
большое"
"""
# month = int(input('Enter month'))
# month_1 = list(range(1,13))
# result = ""
#
# if month in month_1:
#     if month <= 2 or month == 12:
#         result = 'зима'
#
#     elif 3<= month <=5 :
#         result = 'весна'
#
#     elif 6<= month <=8 :
#         result = 'лето'
#
#     elif 9<= month <=11 :
#         result = 'осень'
#     print(result.upper())
# elif month < 1:
#     print('значение слишком маленькое')
# elif month > 12:
#     print('значение слишком большое')

"""4. Дана строка из 6-ти цифр. Проверьте,
что сумма первых трех цифр равняется сумме
вторых трех цифр. Если это так - выведите
'да', в противном случае выведите 'нет'."""
# numbers_string = input('Enter numb') #строку можно ввести. Строка вида "123456", сумма первых трех 1+2+3=6, вторых - 4+5+6=15
# result = "" # по итогу должен быть да или нет
#
# numb_1 = numbers_string[0]+numbers_string[1]+numbers_string[2]
# numb_2 = numbers_string[3]+numbers_string[4]+numbers_string[5]
#
# if numb_1 == numb_2:
#     result = 'Yes'
# else:
#     result = 'No'
# print(result.capitalize())

"""5. Выведите фразы "Greeting №number",
где number - это номер выведенного сообщения,
ровно столько раз, сколько скажет пользователь.
Желательно решить задачу через интерполяцию строк.
"""
# greeting_max_number = int(input('Enter your number message')) # пользователь вводит, сколько раз вывести сообщения
# text = 'Greeting'
# counter = 1
#
# while counter <= greeting_max_number:
#     message = f'{text} № {counter}'
#     print(message)
#     counter += 1


"""6. Необходимо вывести на экран таблицу умножения на 3:
3*1=3
3*2=6
3*3=9
3*4=12
3*5=15
3*6=18
3*7=21
3*8=24
3*9=27
3*10=30
Задачу так же желательно решить, используя интерполяцию строк.
"""
# text_1 = '3'
# counter = 1
# result = 0
# while counter <= 10:
#     result = 3 * counter
#     message = f'{text_1} * {counter} = {result}'
#     print(message)
#     counter += 1


"""7. (extra) Даны два числа.
Определить цифры, входящие в запись
как первого так и второго числа.
Для 125 и 5627 - это 2 и 5,
Для 99999 и 999 - это только 9"""

# number_1 = set(str(125))
# number_2 = set(str(5627))
# number_3 = set(str(99999))
# number_4 = set(str(999))
#
# allset_1 = number_1 & number_2
# print(allset_1)
# allset_2 = number_3 & number_4
# print(allset_2)


"""8. Отгадать целое число,
которое "загадал" компьютер в определенном диапазоне.
Пользователь вводит число, если число больше, чем загаданное,
то компьютер пишет "меньше", если меньше загаданного, то "больше".
И так до тех пор, пока пользователь не угадает число."""

# import random
# secret_number = random.randint(0, 100)
# number = None
#
# while number != secret_number:
#     number = int(input('Enter your number: '))
#     if number > secret_number:
#         print('меньше')
#
#     elif number < secret_number:
#         print('больше')
#
# print('You WIN!!!')

"""9. Найдите сумму чисел в структуре.
"""
# numbers_list = [1, 2, 3,"4",
#                 5, 6, 7, 43,
#                 "5788", 432,
#                 "56654", 45,
#                 111, 223, 12]
#
# numbers_list_int = [int(number) for number in numbers_list]
# sum = 0
# for number in numbers_list_int:
#     sum += number
# print(sum)


"""10. Выведите сумму всех значений словаря."""

# name_age_map = {"Bob": 3, "Alice": 2}
# sum = 0
# for number in name_age_map.values():
#     sum += number
# print(sum)

"""11. Сделайте операции с уже полюбившимся словарем =)."""
team_info = team_info = {
    "squadName": "Super hero squad",
    "homeTown": "Metro City",
    "formed": 2022,
    "secretBase": "Super tower",
    "active": True,
    "members": [
        {
            "name": "Molecule Man",
            "age": 29,
            "secretIdentity": "Dan Jukes",
            "powers": [
                "Radiation resistance",
                "Turning tiny",
                "Radiation blast"
            ]
        },
        {
            "name": "Madame Uppercut",
            "age": 39,
            "secretIdentity": "Jane Wilson",
            "powers": [
                "Million tonne punch",
                "Damage resistance",
                "Superhuman reflexes"
            ]
        },
        {
            "name": "Eternal Flame",
            "age": 1000000,
            "secretIdentity": "Unknown",
            "powers": [
                "Immortality",
                "Heat Immunity",
                "Inferno",
                "Teleportation",
                "Interdimensional travel"
            ]
        }
    ]
}

# 11.1 посчитайте средний возраст всех участников,
# не используя конкретные индексы

# sum = 0
# i=0
# for member in team_info.get('members')[i].values():
#     i +=1
#     sum = print(member)

# 11.2 Посчитайте среднее количество
# количество суперсил у героев.

members = team_info.get('members')
powers_count = 0

for member in members:
    powers = member ['powers']
    powers_count += len(powers)

avg_powers = powers_count/ len(members)
print(avg_powers)




"""12. Перепишите программу, которую мы писали
раньше так, чтобы остался только один print.
"""

# username: str = input("Введи свое имя: ")
# country: str = input("Введи свою страну: ")
# town: str = input("Введи свой город: ")
# street: str = input("Введи свою улицу: ")
# home: str = input("Введи свой дом: ")
# text_1 = "живет по следующему адресу:"
# text_2 = "Спасибо за доверие"
#
# print(f'{username}, {text_1} {country}, {town}, {street}, {home}. {text_2}, {username}!')

