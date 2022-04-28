"""1. Увеличте все элементы
следующей коллекции на 1"""
# int_list = [1,2,"3",4,5,6,7,"5", "100"]

# def foo(item):
#     return int(item)
# def plus(int):
#     return int+1
#
# clear_list = list(map(foo, int_list))
# result_list = list(map(plus, clear_list))
# print(result_list)


"""2. Сложите все элементы
предыдущей коллекции(result_list)"""

# sum_list = sum(result_list)
# print(sum_list)

"""3. Напишите функцию, которая получает
список элементов(аргументом может быть
список как int_list из задания 1). Найдите
сумму всех элементов. И верните как результат
строку:
"Сумма элементов {все элементы списка через запятую} равно {сумма всех элементов}"
"""

# int_list = [1,2,"3",4,5,6,7,"5", "100"]
# def foo(item):
#     return int(item)
#
# def my_list(items, sep: str):
#     items = list(map(foo, items))
#     sum_items = sum(items)
#     result = f'Сумма элементов {sep.join(map(str, items))} равно {sum_items}'
#     return result
# print(my_list(int_list, sep = ', '))


"""4. Перепишите предыдущую функцию,
чтобы она принимала не лист, а
элементы поотдельности. Количество аргументов
должно быть неограниченно."""

numb1 = 1
numb2 = 2
numb3 = 16
numb4 = '8'

def foo(item):
    return int(item)
def my_list(*items, **format_items):
    sep = format_items.get("sep", "")
    items = list(map(foo, items))
    sum_items = sum(items)
    clear_values = f'Сумма элементов {sep.join(map(str, items))} равно {sum_items}.'
    return clear_values
print(my_list(numb1,numb2,numb3,numb4, sep=", "))


"""5. Напишите функцию, которая будет
последовательно перемножать элементы
2х коллекций.
Например a=[1,2,3], b=[3,4,5], то
результат функции - [3, 8, 15].
Предпологается, что коллекции имеют
одинаковое количество элементов."""

# a=[1,2,3]
# b=[3,4,5]
#
# def new_list (first_list, second_list):
#     result = [first_list[i]*second_list[i] for i in range(len(first_list))]
#     return result
# print(new_list(a,b))








