# 1. Напишите программу, которая получает от пользователя имя, его вес и рост.
# И выводит следующее сообщение: "Привет username! Твой имт - bmi!"
# ИМТ = m/(h**2), где: m — масса тела в килограммах, h — рост в метрах.

# username = input('Введите своё имя: ')
# weight = input('Введите свой вес(кг): ')
# height = input('Введите свой рост(м): ')
# bmi = int(weight)/(float(height)**2)
# print('Ваш ИМТ равен: ', bmi)
#
# # 2. Сделайте программу, которая будет запрашивать имя, страну, город, улицу и дом пользователя.
# # А потом выводить сообщение
# # "username живет по слудующему адресу: country, town, street, home. Спасибо за доверие, username!"
# # Решите задачу, не исользуя конкатенацию строк!
#
# username: str = input('Введите своё имя: ')
# country: str = input('Введите свою страну: ')
# town: str = input('Введите свой город: ')
# street: str = input('Введите свою улицу: ')
# home: str = input('Введите свой номер дома: ')
# print(username, 'живет по следующему адресу:', end=(' '))
# print(country,town,street,home, sep=(', '), end=('. '))
# print('Спасибо за доверие,',username, end=('!'))
#
#
# # 3. Выберите структуру данных для задач разработчиков,
# # с условием того, что должна быть возможность легко
# # добавлять задачи и удалять их (примеры задач:
# # "поменять цвет кнопки ввод", "поменять цвет кнопки отправить"),
# # после добавьте еще 2 задачи, удалите самую первую и
# # выведите последнюю добавленную задачу.
#
# tasks = ["поменять цвет кнопки ввод", "поменять цвет кнопки отправить"]
# tasks.append("направить запрос")
# tasks.append("провести рабочую встречу")
# tasks.pop(0)
# print(tasks[-1])
#
# # 4. Упакуйте следующие элементы в коллекцию,
# # с условием того что email должен быть уникальным.
# # После, добавьте еще 2 email-a и удалите email "test@test.com"
#
# user_email1 = "test@test.com"
# user_email2 = "qwerty@qwerty.com"
# emails = {user_email1, user_email2}
# emails.remove("test@test.com")
# print(emails)
#
# # 5. Вы пишите программу, для слияния 2-х IT-компаний.
# # Слияние компаний подразумевает и слияние отдетлов.
# # Однако в итоговой компании должны отсуствовать
# # повторяющиеся отделы, а также должна отсуствовать
# # возможность как-либо изменять финальные отделы.
# companies_departments = [
#     ["development", "QA", "sales", "marketing"], # департаменты первой компании
#     ["devops", "QA", "management", "development"] # департаменты второй компании
# ]
# merged_departments = companies_departments[0]+companies_departments[1] # подберите подходящую структуру данных
# merged_departments = set(merged_departments)
# merged_departments = tuple(merged_departments)
# print(merged_departments)
#
# # 6. Сделайте следующее сообщение в одну строку:
# # "У пользователя Kolia имеются следующие права: read, write, execute!"
#
# username = "Kolia"
# permissions = ["read", "write", "execute"]
#
# print("У пользователя", username, "имеются следующие права:", end=(' '))
# print(permissions[0], permissions[1], permissions[2], sep=(', '), end=('!'))
#
# # 7. Вычислите сколько в среднем сотрудников в каждом отделе
#
# employees = ["Alex", "Tania", "Andry", "Vlad", "Alina", "Vika"]
# departments_number = "3"
#
# avg_employees_per_dep = len(employees)//int(departments_number)
# print(avg_employees_per_dep)

# 8. (extra)
# Найдите ошибки в следующей программе и исправьте их
# users = [1,2,3,4,5,6,7]
# Всем пользователям выдали разрешение на запись
# users_with_write_perm = list(users)
# Пояивились новые пользователи:
# users.append(8)
# users.append(9)

# Им так же выдали разрешение на запись
# users_with_write_perm.append(8)
# users_with_write_perm.append(9)

# Потом прошло какое-то время и решили
# забрать у нескольких пользователей разрешение на запись
# users_with_write_perm.pop(0)
# users_with_write_perm.pop(0)
# users_with_write_perm.pop(0)
# users_with_write_perm.pop(0)
# а потом решили посчитать, сколько процентов сотрудников имеют разрешение на запись:
#percentage_with_perm = len(users_with_write_perm)/len(users) * 100 #подставьте корректную формулу
                                                                # сделайте так, чтобы программа работала
                                                                # и верно считала процент людей с разрешением на запись
#print(percentage_with_perm, '%')

# 9. Создайте коллекцию со словами
# и их частотой встречи в тексте.

# words_frequency = {'mom' : 2, 'dad' : 6, 'sister' :9}
# print(words_frequency)


# 10. Увеличьте количество баллов игрока Bob
# на 7, уменьшете баллы Alice на 10. Добавьте
# Mike в игру со счетом по умолчанию. Удалите
# из игры Kate. Потом получите всех игроков
# отдельно, и посчитайте их количество.
# (для изменения баллов игроков постарайтесь
# использовать сокращенную форму присваивания:
# a += 1 и т.д.)


# default_score = 10
# game_score = {"Bob": 20, "Alice": 40, "Kate": 0}
# game_score['Bob'] += 7
# game_score['Alice'] -=10
# game_score['Mike'] = default_score
# game_score.pop('Kate')
#
# all_players = list(game_score.keys())
# all_players = len(all_players)
# print(all_players)

# 11. Объедините следующие коллекции в одну.

# from uuid import uuid4

# workers_uuids = [str(uuid4()), str(uuid4()), str(uuid4())]
# vacations = [10, 23, 10]
#
# workers_uuids = set(workers_uuids)
# vacations = set(vacations)
#
# workers_vocations = workers_uuids | vacations
# print(workers_vocations)


"""12. Постройте коллекцию, представляющию собой
главы и подглавы книги.
"""
# book_content = {'chapter_1' : ['subchapter_1', 'subchapter_2'],
#                 'chapter_2' : ['subchapter_1', 'subchapter_2'],
#                 'chapter_3' : ['subchapter_1', 'subchapter_2'],
#                 }
# print(book_content)

"""13. Выполните операции над словарем.
"""
team_info = {
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
# занесите в переменную homeTown героев
home_town = [team_info["members"][0]['name'], team_info.get('members')[1].get('name'), team_info.get('members')[2].get('name')]

# получите последнюю суперсилу пользователя "Molecule Man"
molecule_man_last_superpower = team_info.get('members')[0].get("powers")[2]

# вытолкните(удалите ее из списка и поместите в переменную)
# первую суперсилу последнего супергероя
last_supehero_first_superpower = team_info.get('members')[2].get('powers')[0]
team_info.get("members")[2].get('powers').pop(0)
# print(team_info["members"][2]['powers'][0])

# занесите в коллекцию названия всех параметров (name, age...)
# одного из супегероев
params = list(team_info["members"][1])

params_1 = team_info["members"][1].keys()
print(params_1)


# уменьшите значение age супергероя "Eternal Flame" в 2 раза
# (используйте сокращенную форму присваивания)
team_info['members'][2]['age'] //= 2
# print(team_info['members'][2]['age'])

# Получите значения всех полей супергероя "Molecule Man"

# molecule_man_characteristics = (team_info["members"][0]['name'], team_info["members"][0]["age"],
#                                      team_info["members"][0]["secretIdentity"], team_info["members"][0]["powers"],
#                                      )
# print(molecule_man_characteristics)
# molecule_man_characteristics = (team_info.get("members")[0].get("name"), team_info.get("members")[0].get("age"),
#                                 team_info.get("members")[0].get("secretIdentity"), team_info.get("members")[0].get("powers"))

molecule_man_characteristics = team_info.get("members")[0].values()
print(molecule_man_characteristics)

# посчитайте количество героев в команде
heroes_count = len(team_info['members'])
# print(heroes_count)

# Посчитайте средний возраст героя в команде
avg_hero_age = (team_info['members'][0]['age']+team_info['members'][1]['age']+team_info['members'][2]['age'])/heroes_count
# print(avg_hero_age)

# (extra) раскомментируйте код ниже, и сделайте так,
# чтобы он не вызывал ошибку, не изменяя(!) ключи
# team_info["memberes"][0]["poweres"][-1]

