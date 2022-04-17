# 1. Напишите программу, которая получает от пользователя имя, его вес и рост.
# И выводит следующее сообщение: "Привет username! Твой имт - bmi!"
# ИМТ = m/(h**2), где: m — масса тела в килограммах, h — рост в метрах.

username = input('Введите своё имя: ')
weight = input('Введите свой вес(кг): ')
height = input('Введите свой рост(м): ')
bmi = int(weight)/(float(height)**2)
print('Ваш ИМТ равен: ', bmi)

# 2. Сделайте программу, которая будет запрашивать имя, страну, город, улицу и дом пользователя.
# А потом выводить сообщение
# "username живет по слудующему адресу: country, town, street, home. Спасибо за доверие, username!"
# Решите задачу, не исользуя конкатенацию строк!

username: str = input('Введите своё имя: ')
country: str = input('Введите свою страну: ')
town: str = input('Введите свой город: ')
street: str = input('Введите свою улицу: ')
home: str = input('Введите свой номер дома: ')
print(username, 'живет по следующему адресу:', end=(' '))
print(country,town,street,home, sep=(', '), end=('. '))
print('Спасибо за доверие,',username, end=('!'))


# 3. Выберите структуру данных для задач разработчиков,
# с условием того, что должна быть возможность легко
# добавлять задачи и удалять их (примеры задач:
# "поменять цвет кнопки ввод", "поменять цвет кнопки отправить"),
# после добавьте еще 2 задачи, удалите самую первую и
# выведите последнюю добавленную задачу.

tasks = ["поменять цвет кнопки ввод", "поменять цвет кнопки отправить"]
tasks.append("направить запрос")
tasks.append("провести рабочую встречу")
tasks.pop(1)
print(tasks[2])

# 4. Упакуйте следующие элементы в коллекцию,
# с условием того что email должен быть уникальным.
# После, добавьте еще 2 email-a и удалите email "test@test.com"

user_email1 = "test@test.com"
user_email2 = "qwerty@qwerty.com"
emails = {user_email1, user_email2}
emails.remove("test@test.com")
print(emails)

# 5. Вы пишите программу, для слияния 2-х IT-компаний.
# Слияние компаний подразумевает и слияние отдетлов.
# Однако в итоговой компании должны отсуствовать
# повторяющиеся отделы, а также должна отсуствовать
# возможность как-либо изменять финальные отделы.
companies_departments = [
    ["development", "QA", "sales", "marketing"], # департаменты первой компании
    ["devops", "QA", "management", "development"] # департаменты второй компании
]
merged_departments = companies_departments[0]+companies_departments[1] # подберите подходящую структуру данных
merged_departments = set(merged_departments)
merged_departments = tuple(merged_departments)
print(merged_departments)

# 6. Сделайте следующее сообщение в одну строку:
# "У пользователя Kolia имеются следующие права: read, write, execute!"

username = "Kolia"
permissions = ["read", "write", "execute"]

print("У пользователя", username, "имеются следующие права:", end=(' '))
print(permissions[0], permissions[1], permissions[2], sep=(', '), end=('!'))

# 7. Вычислите сколько в среднем сотрудников в каждом отделе

employees = ["Alex", "Tania", "Andry", "Vlad", "Alina", "Vika"]
departments_number = "3"

avg_employees_per_dep = len(employees)//int(departments_number)
print(avg_employees_per_dep)

# 8. (extra)
# Найдите ошибки в следующей программе и исправьте их
users = [1,2,3,4,5,6,7]
# Всем пользователям выдали разрешение на запись
users_with_write_perm = list(users)
# Пояивились новые пользователи:
users.append(8)
users.append(9)

# Им так же выдали разрешение на запись
users_with_write_perm.append(8)
users_with_write_perm.append(9)

# Потом прошло какое-то время и решили
# забрать у нескольких пользователей разрешение на запись
users_with_write_perm.pop(0)
users_with_write_perm.pop(0)
users_with_write_perm.pop(0)
users_with_write_perm.pop(0)
# а потом решили посчитать, сколько процентов сотрудников имеют разрешение на запись:
percentage_with_perm = len(users_with_write_perm)/len(users) * 100 #подставьте корректную формулу
                                                                # сделайте так, чтобы программа работала
                                                                # и верно считала процент людей с разрешением на запись
print(percentage_with_perm, '%')


